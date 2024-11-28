from rest_framework.serializers import ModelSerializer

from order.models import Order, OrderItem


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']

    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        order.calculate_total_price()
        return order


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'order',  'price', 'product', 'total_price']
        read_only_fields = ['total_price', 'id', 'price']

    def create(self, validated_data):
        product = validated_data['product']
        order = validated_data['order']
        quantity = validated_data['quantity']
        price = product.price
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price,
        )
        order.calculate_total_price()
        return order_item


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']





