from django.urls import path
from .views import OrderCreateView

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='create_order'),
]
