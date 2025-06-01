
from django.urls import path
from . import views



app_name = "public"
urlpatterns = [

    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("personalized_orders/", views.personalized_orders, name="personalized_orders"),
    path("events/", views.events, name="events"),

]