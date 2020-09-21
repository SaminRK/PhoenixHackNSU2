from django.db import models

from organisations.models import Organisation

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    source = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True, related_name='source')
    owner = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    unitPrice = models.DecimalField(max_digits=100, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    unit = models.CharField(max_length=20, blank=True)
    isForSale = models.BooleanField(null=False)

    def __str__(self):
        return self.name    
    
class ProductList(models.Model):
    description = models.CharField(max_length=254)

    def __str__(self):
        return self.description

class ProductsInProductList(models.Model):
    productList = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=100, decimal_places=1)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return "%d %s of %s in %s" % (self.quantity, self.unit, self.product.name, self.productList.description)