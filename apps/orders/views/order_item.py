from rest_framework.viewsets import ModelViewSet
from apps.orders.models import OrderItem
from apps.orders.serializers.order_item import OrderItemSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer