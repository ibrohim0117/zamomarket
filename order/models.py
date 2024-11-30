from django.core.validators import MinValueValidator
from django.db import models

from user.models import BaseCreatedModel


class Order(BaseCreatedModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        ],
        default='pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total_price(self):
        total = sum(item.total_price for item in self.order_items.all())
        self.total_price = total
        self.save()

    def __str__(self):
        return self.user.username



class OrderItem(BaseCreatedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @property
    def total_price(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.product.name}, Order: {self.order.id}"






