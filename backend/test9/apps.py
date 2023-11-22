from django.apps import AppConfig


class Test9Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test9'

# Something shady is appearing there, why the prod pipeline triggers on dev?