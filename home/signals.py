from home.models import Prediction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from worker.profile_worker import delete_pic
import random as rd
import asyncio


@receiver(pre_save, sender=Prediction)
def handle_xray_file(sender, instance=None, **kwargs):
    if instance.pred_id is None:
        pic = instance.xray_file
        num = 10**4
        pk = instance.user.pk
        instance.xray_file.name = f'user/xu-{pk}-0{num - pk * pk // 10 ** 2 }/xray-file/tf-{rd.random()*rd.randint(2,10*3)}-{pic.name[-30:]}'
        print("Attribute 'xray_file' has been modified.")
    else:
        instance.xray_file = Prediction.objects.get(pk=instance.pred_id).xray_file



