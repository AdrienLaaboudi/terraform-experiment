from django.apps import AppConfig


class Test9Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test9'

# Something shady is happening here, why do the prod pipeline triggers on dev?
