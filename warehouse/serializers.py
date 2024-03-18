from rest_framework import serializers
from .models import Material, Product

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['warehouse', 'material_name', 'qty', 'price']

class ProductSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_name', 'qty', 'materials']
