from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('root/admin/', admin.site.urls),
    path('user/', include('accounts.urls'), name='accounts'),
    path('', include('home.urls'), name='home'),
    
]


