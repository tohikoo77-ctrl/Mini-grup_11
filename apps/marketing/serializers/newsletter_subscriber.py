from rest_framework import serializers
from apps.marketing.models import NewsletterSubscriber


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"