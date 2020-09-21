from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class UserOrganisation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s works in %s" % (self.user.username , self.user.last_name, self.organisation.name)