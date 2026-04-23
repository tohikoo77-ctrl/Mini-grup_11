from parler_rest.serializers import TranslatableModelSerializer
from apps.notifications.models import Notification


class NotificationSerializer(TranslatableModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"