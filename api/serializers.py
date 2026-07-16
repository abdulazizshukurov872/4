from rest_framework import serializers
from .models import Product

class ProductSerializersz(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at', 'updated_date', 'created_date']
        read_only_fields = ['id', 'created_at',]