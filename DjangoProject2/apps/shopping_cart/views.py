
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from DjangoProject2.apps.public.models import Product
from .cart import Cart

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart.add(product=product, quantity=quantity)

    return redirect('public:shop')