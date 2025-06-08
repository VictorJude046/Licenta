from django.contrib import admin
from .models import Product, ProductImage

# This tells the admin to allow adding multiple images
# on the same page as the product.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # How many extra empty fields to show

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

# We also register ProductImage so it can be managed separately if needed.
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass