from rest_framework.serializers import ModelSerializer

from order.models import Order


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']

    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        order.calculate_total_price()
        return order





