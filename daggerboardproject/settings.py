"""
Django settings for daggerboardproject project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import environ

# read .env file
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '==_xv2k%xqvnf2zwlgpi2b+=rhq*gymuv58uz4%vbd=2h0fq+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'daggerboard.apps.DaggerboardConfig',
    'compressor',
    'django_rq',
    'corsheaders',
    'grading',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'daggerboardproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'daggerboard/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'csp.context_processors.nonce',
            ],
        },
    },
]

WSGI_APPLICATION = 'daggerboardproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'daggerboard',
    'USER': 'daggeradmin',
    'PASSWORD': env('DBPASSWORD'),
    'HOST': env('DBHOST'),
    'PORT': '3306'
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Authentication backends for LDAP and Local Authentication using django Model
AUTHENTICATION_BACKENDS = [
    "daggerboard.ldap.GroupLDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


#support for compressing SCSS into CSS
STATICFILES_FINDERS = [
'compressor.finders.CompressorFinder'
]

COMPRESS_PRECOMPILERS = (
('text/x-scss', 'django_libsass.SassCompiler'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'daggerboard/static')
STATIC_URL = '/static/'
SASS_PRECISION = 8
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'daggerboard/static')]
COMPRESS_ROOT = BASE_DIR + '/daggerboard/static'

## media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'


# login logout
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'

# CSP Policy
CSP_DEFAULT_SRC = [
    "'self'",
    "ajax.googleapis.com",
    'code.jquery.com',
    'cdnjs.cloudflare.com',
    'cdn.datatables.net',
    'cdn.jsdelivr.net',
]

CSP_STYLE_SRC = [
    "'self'",
    'use.fontawesome.com',
    'fonts.googleapis.com',
]

CSP_FONT_SRC = [
    "'self'",
    "cdnjs.cloudflare.com",
    "fonts.gstatic.com",
    "use.fontawesome.com",
]

CSP_SCRIPT_SRC = [
    "'self'",
    "cdnjs.cloudflare.com",
    "code.jquery.com",
    "cdn.jsdelivr.net",
    "ajax.googleapis.com",
    "cdn.datatables.net",
]

## django-rq redis config
RQ_QUEUES = {
    'default': {
        'HOST': env('REDISHOST'),
        'DB': 0,
        'PORT': 6379,
        'PASSWORD': env('REDISPWD'),
        'DEFAULT_TIMEOUT': 360,
    }
}
RQ_SHOW_ADMIN_LINK = True

## CORS headers
CORS_ALLOWED_ORIGINS = [

]

## session cookie
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True