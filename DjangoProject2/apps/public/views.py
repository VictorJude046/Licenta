from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Product
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
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    image_urls = []
    # This check is now safer. It checks if the attribute exists before accessing it.
    if hasattr(product, 'cover_image') and product.cover_image:
        image_urls.append(product.cover_image.url)

    # This check is also safer.
    if hasattr(product, 'images'):
        for p_image in product.images.all():
            image_urls.append(p_image.image.url)

    context = {
        'product': product,
        'image_urls_json': json.dumps(image_urls)
    }
    return render(request, 'product_detail.html', context)
def personalized_orders(request):
    return render(request, "personalized_orders.html")
