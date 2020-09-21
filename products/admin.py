from django.contrib import admin

from .models import Product, Inventory, ProductList, ProductsInProductList

# Register your models here.
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(ProductList)
admin.site.register(ProductsInProductList)