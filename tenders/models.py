from django.db import models

from organisations.models import Organisation
from products.models import ProductList

# Create your models here.
class Tender(models.Model):
    issuerOrganisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    productList = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return "%s -- %s" % (self.issuerOrganisation.name, self.description)

class TenderBid(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    bidderOrganisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    productList = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return "%s -- %s" % (self.bidderOrganisation.name, self.tender.id)
    