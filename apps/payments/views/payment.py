from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Payment
from apps.payments.serializers.payment import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
