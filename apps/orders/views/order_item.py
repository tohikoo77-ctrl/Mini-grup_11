from rest_framework.viewsets import ModelViewSet
from apps.orders.models import OrderItem
from apps.orders.serializers.order_item import OrderItemSerializer
from apps.orders.filters import OrderItemFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OrderItemFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'