from django.contrib import admin
from django.urls import path
from .views import ProductListView, CategoryListView, SubCategoryListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categores/', CategoryListView.as_view(), name='category_list'),
    path('subcategores/', SubCategoryListView.as_view(), name='subcategory_list'),
]
