from django.contrib import admin

from order.models import Order, OrderItem

# admin.site.register(Order)
admin.site.register(OrderItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'status', 'total_price']
    search_fields = ['user__username']
