from rest_framework.viewsets import ModelViewSet
from apps.payments.models import TopUp
from apps.payments.serializers.top_up import TopUpSerializer


class TopUpViewSet(ModelViewSet):
    queryset = TopUp.objects.all()
    serializer_class = TopUpSerializer
