from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Order
from apps.orders.serializers.order import OrderSerializer
from apps.orders.filters import OrderFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(ModelViewSet):
    """ViewSet for managing orders."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OrderFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        """Return queryset with ordering"""
        qs = super().get_queryset()
        return qs.select_related("profile")