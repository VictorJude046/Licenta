
from django.db import models

class HomepageSettings(models.Model):
    hero_title = models.CharField(max_length=200, help_text="The main title displayed on the homepage banner.")
    hero_subtitle = models.TextField(blank=True, help_text="The smaller text displayed below the main title.")

    class Meta:
        verbose_name = "Homepage Settings"
        verbose_name_plural = "Homepage Settings"

    def __str__(self):
        return "Homepage Settings"