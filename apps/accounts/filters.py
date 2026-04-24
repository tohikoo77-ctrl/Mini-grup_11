from apps.accounts.models import User, Language, Profile, UserConfirmation
from apps.shared.filters import make_filter

UserFilter = make_filter(User)
LanguageFilter = make_filter(Language)
ProfileFilter = make_filter(Profile)
UserConfirmationFilter = make_filter(UserConfirmation)
