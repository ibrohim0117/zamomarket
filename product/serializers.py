from rest_framework import serializers

from product.models import Product, Category, SubCategory, Comment, Cart


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug',  'count', 'sale', 'subcategory', 'is_active']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=25, read_only=True)
    user = serializers.CharField(max_length=25, read_only=True)
    username = serializers.CharField(max_length=25, read_only=True)

    class Meta:
        model = Comment
        fields = ['product', 'user', 'rating', 'username', 'text']


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'user', 'rating', 'username', 'text']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'now_price', 'total_price']


