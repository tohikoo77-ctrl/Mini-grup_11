from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import UserNotification
from apps.notifications.serializers.user_notification import UserNotificationSerializer


class UserNotificationViewSet(ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer