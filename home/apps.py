from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        from home.signals import handle_xray_file, pre_save, Prediction

        pre_save.connect(handle_xray_file, sender=Prediction)