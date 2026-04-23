from parler_rest.serializers import TranslatableModelSerializer
from apps.payments.models import PaymentType


class PaymentTypeSerializer(TranslatableModelSerializer):
    class Meta:
        model = PaymentType
        fields = "__all__"
