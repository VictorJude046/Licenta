from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Product,Category
import json

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
    category_id = request.GET.get('category')
    sort_by = request.GET.get('sort')

    products = Product.objects.all()
    categories = Category.objects.all()


    if category_id:
        products = products.filter(category_id=category_id)
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'name_asc':
        products = products.order_by('name')
    elif sort_by == 'name_desc':
        products = products.order_by('-name')

    context = {
        'products': products,
        'categories': categories,
        'selected_category_id': category_id,
        'selected_sort': sort_by,
    }
    return render(request, 'shop.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    image_urls = []

    if product.image:
        image_urls.append(product.image.url)

    for p_image in product.images.all():
        image_urls.append(p_image.image.url)


    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]

    context = {
        'product': product,
        'image_urls_json': image_urls,
        'related_products': related_products, # <-- Add related_products to the context
    }
    return render(request, 'product_detail.html', context)
def personalized_orders(request):
    return render(request, "personalized_orders.html")
