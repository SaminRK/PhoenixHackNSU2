from django.contrib import admin

from .models import Product, ProductList, ProductsInProductList

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductList)
admin.site.register(ProductsInProductList)