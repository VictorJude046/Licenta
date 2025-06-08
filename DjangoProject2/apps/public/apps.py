from django.apps import AppConfig


class PublicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # This line MUST match the full path to your app directory
    name = 'DjangoProject2.apps.public'