from django.apps import AppConfig


class MyFirstSubappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_first_subapp'
