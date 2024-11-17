from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from product.filters import ProductFilter
from product.models import Product, SubCategory, Category, Comment
from product.serializers import (
    ProductListSerializer, SubCategoryListSerializer,
    CategoryListSerializer, CommentCreateSerializer, CommentListSerializer
)


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


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug=slug)
        # print(slug)
        # print(product)
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        serializer.save(product=product, user=user)
        super().perform_create(serializer)


class ProductCommentListView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        try:
            product = Product.objects.get(slug=slug)
        except:
            raise NotFound(detail="Product not found")
        data = Comment.objects.filter(product=product)
        return data
