from django.contrib import admin
from .models import ProdctImage, Product


class ProductImageInline(admin.TabularInline):
    model = ProdctImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProdctImage)