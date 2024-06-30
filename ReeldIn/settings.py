"""
Django settings for ReeldIn project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see:
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.core.mail import mail_admins
from dotenv import load_dotenv

# Obtain the base directory of the project and use it to build the path to the .env file
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path, override=True)

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Load environment variables
SECRET_KEY = os.environ.get("SECRET_KEY")
DDD_API_KEY = os.environ.get("DDD_API_KEY")
TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
WATCHMODE_API_KEY = os.environ.get("WATCHMODE_API_KEY")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = GMAIL_PASSWORD
EMAIL_USE_TLS = True
SERVER_EMAIL = "reeldin.staff@gmail.com"

DEBUG = os.environ.get("DEBUG") == "True"
ADMINS = [("ReeldIn", "reeldin.staff@gmail.com")]

ALLOWED_HOSTS = [
    "reeld.in",
    "www.reeld.in",
    "localhost",
    "reeldin.azurewebsites.net",
    "reeldin.scm.azurewebsites.net",
    "169.254.129.3",  # Web App's IP address
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = ["https://reeld.in", "https://reeldin.azurewebsites.net"]

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = False  # Maybe fixes our issue with CSRF tokens

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

# Application definition

INSTALLED_APPS = [
    "django_browser_reload",
    "theme",
    "tailwind",
    "accounts",
    "landing_page",
    "dashboard",
    "recommendations",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ReeldIn.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ReeldIn.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

if DEBUG:
    STATIC_URL = "/static/"
else:
    STATIC_URL = "https://reeldincdn-evgmbyaye3gehbbt.z02.azurefd.net/static/"

STATIC_ROOT = BASE_DIR / "static"

# Media files (user-uploaded files i.e profile pictures)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "/accounts/login/"

# Tailwind configuration
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
