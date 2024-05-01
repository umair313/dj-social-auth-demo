"""
WSGI config for dj_social_auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from datetime import timedelta

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_social_auth.settings')

application = get_wsgi_application()


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=90),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
}


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_USE_JWT = True

# REST_AUTH_SERIALIZERS = {
#    'USER_DETAILS_SERIALIZER': 'progress.patient.api.serializers.PatientSerializer',
# }

REST_AUTH_TOKEN_MODEL = None
# SOCIALACCOUNT_ADAPTER = 'progress.users.adaptors.CustomSocialAccountAdapter'