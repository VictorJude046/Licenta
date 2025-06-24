from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')

    def __str__(self):
        return f"Image for {self.product.name}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    is_featured = models.BooleanField(default=False, help_text="Check this for the main, top project on the homepage.")
    display_order = models.PositiveIntegerField(default=0, help_text="Projects with a lower number will be displayed first.")

    class Meta:
        ordering = ['display_order'] # Default order for all projects

    def __str__(self):
        return self.title

class ProductImage360(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_360')
    image = models.ImageField(upload_to='product_360/')

    def __str__(self):
        return f"360 Image for {self.product.name}"