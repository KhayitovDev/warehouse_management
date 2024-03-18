from django.db import models

class Warehouse(models.Model):
    title=models.CharField(max_length=25)
    
    def __str__(self):
        return self.title


class Material(models.Model):
    warehouse=models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    material_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.material_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    materials = models.ManyToManyField(Material)
    
    def __str__(self):
        return self.product_name
    
