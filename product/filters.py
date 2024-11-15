from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter, CharFilter

from .models import Product


class ProductFilter(FilterSet):
    category = CharFilter(field_name='subcategory__category__name', lookup_expr='icontains')
    subcategory = CharFilter(field_name='subcategory__name', lookup_expr='icontains')
    price_min = NumberFilter(field_name='price', lookup_expr='gte')
    price_max = NumberFilter(field_name='price', lookup_expr='lte')
    sale_min = NumberFilter(field_name='sale', lookup_expr='gte')
    sale_max = NumberFilter(field_name='sale', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'price_min', 'price_max', 'sale_min', 'sale_max']


