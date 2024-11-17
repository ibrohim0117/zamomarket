from rest_framework import serializers

from product.models import Product, Category, SubCategory, Comment


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug',  'count', 'sale', 'subcategory', 'is_active', 'comments']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    product = serializers.CharField(max_length=25, read_only=True)
    user = serializers.CharField(max_length=25, read_only=True)
    username = serializers.CharField(max_length=25, read_only=True)

    class Meta:
        model = Comment
        fields = ['product', 'user', 'rating', 'username', 'text']