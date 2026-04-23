from datetime import timedelta
import os
from pathlib import Path

import dj_database_url
from django.utils.translation import gettext_lazy as _

from envs import (
    SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_URL,
    CSRF_TRUSTED_ORIGINS, CORS_ALLOWED_ORIGINS,
    EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME,
    REDIS_URL, CELERY_BROKER_URL, CELERY_RESULT_BACKEND, TIME_ZONE
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ALLOWED_HOSTS
INTERNAL_IPS = ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = False

# Application definition
INSTALLED_APPS = [
    'django_daisy',
    'django.contrib.admin',
    'django.contrib.humanize',  # Required for django-daisy
    # default apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'rest_framework_json_api',
    'django_filters',
]

THIRD_APPS = {
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'debug_toolbar',
    'import_export',
    'drf_standardized_errors',
    'schema_viewer',
    'adrf',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rosetta',
    'parler',
    'parler_rest',
    "django_celery_beat",
    "django_celery_results",
}

LOCAL_APPS = [
    'apps.shared',
    'apps.accounts',
    'apps.cart',
    'apps.catalog',
    'apps.common',
    'apps.content',
    'apps.marketing',
    'apps.notifications',
    'apps.orders',
    'apps.payments',
    'apps.reviews',
]

INSTALLED_APPS += THIRD_APPS
INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "apps.shared.middleware.UserLanguageMiddleware",  # ✅ custom
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = "core.asgi.application" # noqa


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": dj_database_url.config(
            default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=DB_URL,  # DB_URL comes from envs.py, e.g. "postgres://user:pass@host:port/dbname"
            conn_max_age=600,
            ssl_require=False
        )
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

TIME_ZONE = TIME_ZONE

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # ⚡ Pagination (JSON:API compatible)
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS": "rest_framework_json_api.pagination.JsonApiPageNumberPagination",

    # 🎨 Renderers (JSON:API first)
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JSONRenderer",
        "rest_framework_json_api.renderers.BrowsableAPIRenderer",  # disable in prod if not needed
    ),

    # 📝 Metadata
    "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",

    # 🔎 Filtering, Ordering, Searching
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework_json_api.filters.QueryParameterValidationFilter",
        "rest_framework_json_api.filters.OrderingFilter",
        "rest_framework_json_api.django_filters.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "SEARCH_PARAM": "filter[search]",

    # 🧪 Testing
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JSONRenderer",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "vnd.api+json",

    # 🔐 Permissions
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        # "# apps.shared.permissions.HasCompletedSignup",
    ),

    # 🔑 Authentication (JWT first)
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",  # useful for docs/dev
    ),

    # 📥 Parsers (JSON:API + fallback)
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework_json_api.parsers.JSONParser",
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),

    # 🚨 Exceptions & Schema
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=ACCESS_TOKEN_LIFETIME),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=REFRESH_TOKEN_LIFETIME),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD

# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Collect static files here
STATIC_ROOT = BASE_DIR / 'staticfiles'

# URL to access static files
STATIC_URL = 'static/'

DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

SPECTACULAR_SETTINGS = {
    'TITLE': 'Barber & Salon | Escape',
    "DESCRIPTION": "Clean/Onion architecture DRF API",
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]/',  # Example: /api/v1/users will get 'users' tag
}

AUTH_USER_MODEL = "accounts.User"

# LANGUAGE_CODE = 'en'

LANGUAGES = (
    ("en", _("English (US)")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
    ("ar", _("Arabic")),
    ("tg", _("Tajik")),
    ("ja", _("Japanese")),
)


LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ru'},
        {'code': 'uz'},
        {'code': 'ar'},
        {'code': 'tg'},
        {'code': 'ja'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

PARLER_DEFAULT_LANGUAGE_CODE = "en"

# Celery
CELERY_BROKER_URL = CELERY_BROKER_URL
CELERY_RESULT_BACKEND = CELERY_RESULT_BACKEND
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ADD_HEADERS_FUNCTION = None

# APPEND_SLASH=False
