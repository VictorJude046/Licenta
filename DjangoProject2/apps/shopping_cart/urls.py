from django.urls import path
from . import views

app_name = 'shopping_cart' # Use the new app name here

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]