"""
Django settings for wiz project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
import cloudinary_storage
import cloudinary

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-j%xpj3hxlv4luf6+*@2q%uxffxoprsc3$-ky8ktt4bt^dldxq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# EMAIL_HOST = 's690.lon1.mysecurecloudhost.com'
# EMAIL_HOST_USER = 'mail@celebritymanagementbookings.com'
# EMAIL_HOST_PASSWORD = '(.{})!7qf$xR'
# DEFAULT_FROM_EMAIL = 'mail@celebritymanagementbookings.com'
# SERVER_EMAIL = 'mail@celebritymanagementbookings.com'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.hostinger.com'
EMAIL_HOST_USER = 'info@managementbookingagencies.icu'
EMAIL_HOST_PASSWORD = 'Aaasssaaa1@'
DEFAULT_FROM_EMAIL = 'info@managementbookingagencies.icu'
SERVER_EMAIL = 'info@managementbookingagencies.icu'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'whitenoise.runserver_nostatic',
    'index',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wiz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
import dj_database_url
DATABASE_URL = 'postgres://edceuqpj:nfVOjhfagg4uTKXFzbCI5atTJH3XSSLI@abul.db.elephantsql.com/edceuqpj'

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =  os.path.join(BASE_DIR, 'static_cdn')
MEDIA_URL = '/media_cdn/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media_cdn')
CRISPY_TEMPLATE_PACK='bootstrap4'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
cloudinary.config( 
  cloud_name = "dfwysasj5", 
  api_key = "717662813998567", 
  api_secret = "YnXh5RkikSNaWUBFtTyQ3MjGhgM",
  secure =True
)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dfwysasj5',
    'API_KEY': '717662813998567',
    'API_SECRET': 'YnXh5RkikSNaWUBFtTyQ3MjGhgM',
    'api_proxy': 'http://proxy.server:3128'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


AUTH_USER_MODEL = 'user.CustomUser'

