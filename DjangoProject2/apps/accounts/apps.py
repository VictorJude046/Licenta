from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "DjangoProject2.apps.accounts"

    def ready(self):
        import DjangoProject2.apps.accounts.signals