from .base import *

DEBUG = False

ADMINS = (
    ('Bohdan K', 'bogdan.kalika@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'bohdan',
        'PASSWORD': 'bohdan',
    }
}


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
