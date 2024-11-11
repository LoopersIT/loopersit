from .base import *
import json
from django.core.exceptions import ImproperlyConfigured


with open('secrets.json') as f:
    secrets = json.load(f)


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)




SECRET_KEY = (get_secret('SECRET_KEY'), 'django-insecure-w1q2!*29ja2_oaj=&!-stm8a5q7!3ymq!knx78h@)%v1-y80fl')


DEBUG = False


ADMINS = (
    ('Sarwar Zahan', 'zahan.ads@gmail.com'),
)


ALLOWED_HOSTS = ['157.230.230.195', 'loopersit.com', 'www.loopersit.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'litdb',
        'USER': 'litdbuser',
        'PASSWORD': get_secret('PGRESS_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_HOST_USER = 'szahan4@gmail.com' 
EMAIL_HOST_PASSWORD = get_secret('MAIL_PASSWORD')
EMAIL_PORT = 587 
EMAIL_USE_TLS = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
# MEDIA_URL = 'https://plant-trends.bsmiab.org/media/'