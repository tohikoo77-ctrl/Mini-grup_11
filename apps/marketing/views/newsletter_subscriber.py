from rest_framework.viewsets import ModelViewSet
from apps.marketing.models import NewsletterSubscriber
from apps.marketing.serializers.newsletter_subscriber import NewsletterSubscriberSerializer


class NewsletterSubscriberViewSet(ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer