from parler_rest.serializers import TranslatableModelSerializer
from apps.notifications.models import UserNotification


class UserNotificationSerializer(TranslatableModelSerializer):
    class Meta:
        model = UserNotification
        fields = "__all__"