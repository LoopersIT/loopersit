from .base import *
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False


# ADMINS = (
#     ('Sarwar Zahan', 'zahan.ads@gmail.com'),
# )


ALLOWED_HOSTS = ['loopersit-final.onrender.com', 'loopersit.com', 'www.loopersit.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'loopdb',
#         'USER': 'loopdbuser',
#         'PASSWORD': os.getenv('PGRESS_PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }


# EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_HOST_USER = 'szahan4@gmail.com' 
# EMAIL_HOST_PASSWORD = os.getenv('MAIL_PASSWORD')
# EMAIL_PORT = 587 
# EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
# MEDIA_URL = 'https://plant-trends.bsmiab.org/media/'