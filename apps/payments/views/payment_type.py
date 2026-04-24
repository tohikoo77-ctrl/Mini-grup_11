from rest_framework.viewsets import ModelViewSet
from apps.payments.models import PaymentType
from apps.payments.serializers.payment_type import PaymentTypeSerializer
from apps.payments.filters import PaymentTypeFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PaymentTypeViewSet(ModelViewSet):
    """ViewSet for managing payment types."""
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PaymentTypeFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
