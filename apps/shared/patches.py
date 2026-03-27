from django.utils import translation
from icecream import ic
from parler.utils.context import switch_language
from parler_rest import serializers as parler_serializers


def _patched_to_representation(self, instance):
    request = self.context.get("request")
    ic(request)

    lang_code = None
    if request and request.user.is_authenticated:
        profile = getattr(request.user, "profile", None)
        lang_code = getattr(getattr(profile, "app_language", None), "code", None)

    if not lang_code:
        lang_code = translation.get_language()

    with switch_language(instance, lang_code):
        return super(parler_serializers.TranslatableModelSerializer, self).to_representation(instance)


# apply monkey-patch
parler_serializers.TranslatableModelSerializer.to_representation = _patched_to_representation