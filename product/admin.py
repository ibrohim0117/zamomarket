from django.contrib import admin

from product.models import Product, Category, SubCategory, Tag, ProductImage, Comment

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'count', 'sale', 'is_active')
    search_fields = ('name', 'price', 'count')
    inlines = [ProductImageInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'username', 'rating', 'text')
