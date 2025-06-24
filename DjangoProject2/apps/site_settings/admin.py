from django.contrib import admin
from .models import HomepageSettings

@admin.register(HomepageSettings)
class HomepageSettingsAdmin(admin.ModelAdmin):
    pass