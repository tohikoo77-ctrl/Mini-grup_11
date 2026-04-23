from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.notification import NotificationViewSet
from .views.user_notification import UserNotificationViewSet
from .views.notification_setting import NotificationSettingViewSet

router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename="notification")
router.register(r"user-notifications", UserNotificationViewSet, basename="user-notification")
router.register(r"notification-settings", NotificationSettingViewSet, basename="notification-setting")

app_name = "notifications"

urlpatterns = [
    path("", include(router.urls)),
]