from django.shortcuts import render, get_object_or_404
import json
from .models import Product, Category, Project
from DjangoProject2.apps.site_settings.models import HomepageSettings


# This is the updated index view that fetches all content for the homepage
def index(request):
    homepage_settings = HomepageSettings.objects.first()
    projects = Project.objects.all().order_by('display_order')

    context = {
        'homepage_settings': homepage_settings,
        'projects': projects,
    }
    return render(request, "index.html", context)


# This is your shop view with filtering and sorting
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


# This is your product detail view with related products
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
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


# These are your other static page views
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def events(request):
    return render(request, "events.html")


def personalized_orders(request):
    return render(request, "personalized_orders.html")



def product_360(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_360.html', {'product': product})

