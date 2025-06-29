"""
URL configuration for DjangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ai_chat


# Define your primary URL patterns first.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("DjangoProject2.apps.public.urls")),
    path("accounts/", include("DjangoProject2.apps.accounts.urls")),
    path("cart/", include("DjangoProject2.apps.shopping_cart.urls")),
    path('ai-chat/', ai_chat, name='ai_chat'),
]

# This is the key change. We add the media URL patterns here,
# BEFORE the catch-all flatpages pattern is added.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The flatpages pattern acts as a "catch-all" and must be added last.
urlpatterns += [
    path("", include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('DjangoProject2.apps.accounts.urls')),  # your custom app
    path('accounts/', include('django.contrib.auth.urls')),
]
