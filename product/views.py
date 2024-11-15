from django.shortcuts import render
from rest_framework.generics import ListAPIView

from product.models import Product
from product.serializers import ProductListSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
