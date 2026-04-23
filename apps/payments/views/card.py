from rest_framework.viewsets import ModelViewSet
from apps.payments.models import Card
from apps.payments.serializers.card import CardSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer