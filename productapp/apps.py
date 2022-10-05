from django.apps import AppConfig


class ProductappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productapp'
    
    #used to Change the App Name In Admin Panel
    verbose_name="Category & Products"
