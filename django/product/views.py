from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import ProductModels


class ProductViewSets(viewsets.ViewSet):
    def list(self, request):
        products = ProductModels.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(ProductModels, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = get_object_or_404(ProductModels, id=pk)
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        product = get_object_or_404(ProductModels, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
