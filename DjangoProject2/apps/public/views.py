from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    print(request.user)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def events(request):
    return render(request, "events.html")


def shop(request):
    return render(request, "shop.html")


def personalized_orders(request):
    return render(request, "personalized_orders.html")
