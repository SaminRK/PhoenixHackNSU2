from django.contrib import admin

from .models import Product, ProductList, ProductsInProductList, Order, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductList)
admin.site.register(ProductsInProductList)
admin.site.register(Inventory)
admin.site.register(Order)