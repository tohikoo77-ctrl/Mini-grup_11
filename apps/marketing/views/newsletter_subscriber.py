from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import NewsletterSubscriber
from apps.marketing.serializers.newsletter_subscriber import NewsletterSubscriberSerializer
from apps.marketing.filters import NewsletterSubscriberFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class NewsletterSubscriberViewSet(ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = NewsletterSubscriberFilter
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'