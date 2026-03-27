from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class UserLanguageMiddleware(MiddlewareMixin):
    """
    Middleware to automatically activate user's preferred language
    based on their profile settings.
    """

    def process_request(self, request):
        # Check if user is authenticated and has language preference
        if (request.user.is_authenticated and
                hasattr(request.user, 'profile') and
                hasattr(request.user.profile, 'app_language') and
                request.user.profile.app_language):

            try:
                user_language = request.user.profile.app_language.code
                translation.activate(user_language)
                # Optional: Set language in request for debugging
                request.LANGUAGE_CODE = user_language
            except AttributeError:
                # Fallback if language code is not available
                pass

        return None