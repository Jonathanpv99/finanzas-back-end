from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Cambia esto con tu origen permitido
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://localhost:5173'
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME':'finanzas',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'