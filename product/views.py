from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from product.filters import ProductFilter
from product.models import Product, SubCategory, Category
from product.serializers import ProductListSerializer, SubCategoryListSerializer, CategoryListSerializer


# rot66rot


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description']



class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer