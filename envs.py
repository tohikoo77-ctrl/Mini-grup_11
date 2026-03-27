import os

from decouple import config, Csv
from icecream import ic

# Check if .env file exists
env_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
ic(env_file_path)
if not os.path.exists(env_file_path):
    ic(f"File not found: {env_file_path}")
    ic('.env fayli topilmadi!')
    ic('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)

SECRET_KEY = config('SECRET_KEY', default='djangorestframework')
DEBUG = config('DEBUG', default=True, cast=bool)
ADMIN_URL = config('ADMIN_URL', default='admin/')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://127.0.0.1', cast=Csv())
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://127.0.0.1', cast=Csv())
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='').replace("-", " ")
API_V1_URL = config('API_V1_URL', default='')
ACCESS_TOKEN_LIFETIME = config('ACCESS_TOKEN_LIFETIME', default=15, cast=int)
REFRESH_TOKEN_LIFETIME = config('REFRESH_TOKEN_LIFETIME', default=1, cast=int)
REDIS_URL = config('REDIS_URL', default='redis://127.0.0.1:6379/1')
DB_URL = config("DB_URL", default="postgres://postgres:admin@localhost:5432/escape")
CELERY_BROKER_URL = config("CELERY_BROKER_URL", default='redis://127.0.0.1:6379/1')
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", default='redis://127.0.0.1:6379/1')

TIME_ZONE = config("TIME_ZONE", default='Asia/Tashkent')
SMS_TOKEN = config("SMS_TOKEN", default='')
SMS_URL = config("SMS_URL", default='')
