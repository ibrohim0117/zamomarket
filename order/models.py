from django.core.validators import MinValueValidator
from django.db import models

from user.models import BaseCreatedModel


class Order(BaseCreatedModel):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=20, choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        ],
        default='pending'
    )

    @property
    def total_price(self):
        self.product.price * self.quantity

    def __str__(self):
        return self.product.name



