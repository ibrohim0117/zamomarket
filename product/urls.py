from django.contrib import admin
from django.urls import path
from .views import (
    ProductListView, CategoryListView,
    SubCategoryListView, CommentCreateView, ProductCommentListView
)

urlpatterns = [
    # product
    path('products/', ProductListView.as_view(), name='product_list'),

    # category
    path('categores/', CategoryListView.as_view(), name='category_list'),

    # subcategory
    path('subcategores/', SubCategoryListView.as_view(), name='subcategory_list'),

    # comment
    path('create-comment/<slug:slug>/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<slug:slug>/', ProductCommentListView.as_view(), name='comment_list'),
]
