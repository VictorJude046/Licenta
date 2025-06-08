from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:product_id>/', views.product_detail, name='product_detail'),
    path('personalized_orders/', views.personalized_orders, name='personalized_orders'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]