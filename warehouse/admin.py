from django.contrib import admin
from .models import Product, Warehouse, Material

# Register your models here.

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Material)