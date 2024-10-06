from rest_framework import serializers
from .models import ProductModels


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModels
        fields = '__all__'
