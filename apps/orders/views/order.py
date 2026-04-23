from rest_framework.viewsets import ModelViewSet
from apps.orders.models import Order
from apps.orders.serializers.order import OrderSerializer


class OrderViewSet(ModelViewSet):
    """
    ViewSet for managing orders.
    Supports:
    - List: Filterable, paginated list
    - Retrieve: Get specific order
    - Create: Place new order
    - Destroy: Cancel order (soft delete)
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """Return queryset with ordering"""
        qs = super().get_queryset()
        return qs.select_related("profile")