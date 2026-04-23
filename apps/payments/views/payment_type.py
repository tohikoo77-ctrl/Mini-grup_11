from rest_framework.viewsets import ModelViewSet
from apps.payments.models import PaymentType
from apps.payments.serializers.payment_type import PaymentTypeSerializer


class PaymentTypeViewSet(ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
