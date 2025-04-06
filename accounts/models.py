from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import CustomUserManager
from django.core.validators import EmailValidator
from accounts.helpers import validators as v
import datetime as dt
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['endpoint_url'] =  settings.ENDPOINT_URL
        kwargs['access_key'] = settings.SUPABASE_ACCESS_KEY
        kwargs['secret_key'] = settings.SUPABASE_SECRET_KEY
        kwargs['bucket_name'] = settings.SUPABASE_BUCKET_NAME
        super().__init__(*args, **kwargs)
        
    def url(self, name):
        # Implement the method to return the URL for a file in Supabase
        return f"{settings.SUPABASE_SERVE_URL}/{settings.SUPABASE_BUCKET_NAME}/{name}"

class User(AbstractUser):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('x', 'Other')
    )
    username = None
    # profile data
    email = models.EmailField(unique=True, validators=[EmailValidator, v.validate_email])
    phone = models.CharField(max_length=10, unique=True, validators=[v.validate_phone])
    first_name = models.CharField(max_length=150, validators=[v.validate_first_name])
    last_name = models.CharField(max_length=150, blank=True, validators=[v.validate_last_name])
    gender = models.CharField(max_length=10, blank=True, choices=GENDER)
    dob = models.DateField(blank=True, null=True)
    profile_pic = models.FileField(upload_to='', null=True, blank=True, storage=SupabaseStorage())
    last_modified = models.DateField(auto_now=True)
    bio = models.TextField(blank=True, null=True)
    # verification detail
    verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6,blank=True, null=True)
    email_otp_ts = models.DateTimeField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    phone_otp = models.CharField(max_length=6,blank=True, null=True)
    phone_otp_ts = models.DateTimeField(blank=True, null=True)
    phone_verified_at = models.DateTimeField(blank=True, null=True)
    # forgot password
    fget_otp = models.CharField(max_length=6,blank=True, null=True)
    fget_token = models.CharField(max_length=100, null=True, blank=True)
    fget_otp_ts = models.DateTimeField(blank=True, null=True)
    last_fget = models.DateTimeField(blank=True, null=True)
    # suspension
    suspended = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name']

    
    class Meta:
        db_table = "Users"
        verbose_name = "User"

    def __str__(self):
        return f'{self.email} : {self.first_name}'
    
    def save(self, *args, **kwargs):
        if not self.email.islower():
            self.email = self.email.lower()
        super().save(*args, **kwargs)
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
    
#Profile Updation code 
# class UserProfile(models.Model):
#     user_name = models.CharField(max_length=100)
#     user_email = models.EmailField(default='johndoe@example.com')
#     user_age = models.IntegerField(default=0)
#     user_bio = models.TextField()
#     user_image = models.ImageField(upload_to='user_profile', blank=True, null=True)
