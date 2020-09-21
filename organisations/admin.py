from django.contrib import admin

from .models import Organisation, UserOrganisation

# Register your models here.
admin.site.register(Organisation)
admin.site.register(UserOrganisation)