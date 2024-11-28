from django.urls import path
from .views import OrderCreateView, OrderItemCreateView, OrderListView

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='create_order'),
    path('orderitem/<int:order_id>/', OrderItemCreateView.as_view(), name='create_order_item'),
    path('order-list/', OrderListView.as_view(), name='order_list'),

]
