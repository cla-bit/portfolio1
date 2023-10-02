# from django.contrib.sitemaps import Sitemap
# from .models import Portfolio, Project, Contact
# from django.urls import reverse
#
#
# class PortfolioSitemap(Sitemap):
#     def items(self):
#         return ['home:home']
#
#     def location(self, item):
#         return reverse(item)
#
#
# class ProjectSitemap(Sitemap):
#     def items(self):
#         return Project.objects.all()
#

# class SkillSitemap(Sitemap):
#     def items(self):
#         return ['home:home']
#
#     def location(self, item):
#         return reverse(item)
#
#
# class ServiceSitemap(Sitemap):
#     def items(self):
#         return ['home:home']
#
#     def location(self, item):
#         return reverse(item)
#
#
# class CategorySitemap(Sitemap):
#     def items(self):
#         return ['home:home']
#
#     def location(self, item):
#         return reverse(item)


"""
Django's settings for claver project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['claver.pythonanywhere.com']


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'home.apps.HomeConfig',
]

THIRD_PARTY_APPS = [
    'jazzmin',
    'widget_tweaks',
]

INSTALLED_APPS = DJANGO_APPS + MY_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'claver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"template"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context-processor.portfolio',
            ],
        },
    },
]

WSGI_APPLICATION = 'claver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('NAME'),
        'HOST': config('HOST'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

ADMINS = [('Peter', config('RECEIVER_EMAIL'))]

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

SERVER_EMAIL = 'root@localhost'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/"static"]
STATIC_ROOT = '/home/claver/portfolio/staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR/"media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = "smtp.gmail.com"   # email host port=smtp.gmail.com / domain name
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # email host user
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # email password
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

SECURE_CROSS_ORIGIN_OPENER_POLICY = None

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# cors settings
CORS_ALLOWED_ORIGINS = ['https://claver.pythonanywhere.com']

# csrf settings
CSRF_TRUSTED_ORIGINS = ['https://claver.pythonanywhere.com']

