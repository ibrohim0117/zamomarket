from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, status

from .models import Order
from .serializers import OrderCreateSerializer, OrderItemSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404

class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=OrderCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({"order_id":order.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=OrderItemSerializer,
    )
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            order_item = serializer.save(order=order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

