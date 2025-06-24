from django.contrib import admin
from .models import Category, Product, ProductImage, Project, ProductImage360

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# admin.py
class ProductImage360Inline(admin.TabularInline):
    model = ProductImage360
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    inlines = [ProductImageInline, ProductImage360Inline]



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'display_order')
    list_editable = ('is_featured', 'display_order')



