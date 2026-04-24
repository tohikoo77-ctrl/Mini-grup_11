from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Payment
from apps.payments.serializers.payment import PaymentSerializer
from apps.payments.filters import PaymentFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PaymentViewSet(ModelViewSet):
    """ViewSet for managing payments."""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PaymentFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
