from rest_framework.permissions import BasePermission


class HasCompletedSignup(BasePermission):
    """
    Allows access if user has completed signup (auth_status == "done")
    or is a superuser/staff.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        return (
            getattr(user, "auth_status", None) == "done"
            or user.is_superuser
            or user.is_staff
        )
