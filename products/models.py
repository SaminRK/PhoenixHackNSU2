from django.db import models

from organisations.models import Organisation

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=100, decimal_places=1)
    unit = models.CharField(max_length=20)
    unitPrice = models.DecimalField(max_digits=100, decimal_places=1)
    isForSale = models.BooleanField()

    def __str__(self):
        return self.name

class ProductList(models.Model):
    description = models.CharField(max_length=254)

class ProductsInProductList(models.Model):
    productList = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=100, decimal_places=1)
    unit = models.CharField(max_length=20)