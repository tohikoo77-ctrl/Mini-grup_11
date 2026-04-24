from apps.orders.models import Order, OrderItem
from apps.shared.filters import make_filter

OrderFilter = make_filter(Order)
OrderItemFilter = make_filter(OrderItem)
