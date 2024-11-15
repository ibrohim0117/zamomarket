from django.contrib import admin

from product.models import Product, Category, SubCategory, Tag

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
