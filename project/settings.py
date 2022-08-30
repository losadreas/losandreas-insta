import os
import django_heroku
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*(-2g3^hehsnq2i#u8@7r**nvps@%6n!)skk*=5^wj8^$$f&f7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = 'post'

AUTH_USER_MODEL = 'user.User'

EMAIL_HOST = 'smtp.ukr.net'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'losandreas-insta@ukr.net'
EMAIL_HOST_PASSWORD = 'OZWB7ufDN2ha8vsk'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'losandreas-insta@ukr.net'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Application definition

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '415886718302-linm93o6oqsc8ukpqgm103jv63ktjuvs.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_GOOGLE_OAUTH2_LOGIN_URL = 'home'

SOCIAL_AUTH_GITHUB_KEY = 'bcb71714360f6bf59e34'
SOCIAL_AUTH_GITHUB_SECRET = '920c553aff841883f5c9a0d6024a1a32d409518c'
SOCIAL_AUTH_GITHUB_LOGIN_URL = 'home'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = 'addition_info'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'login_error'
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email', 'read:user']

SOCIAL_AUTH_URL_NAMESPACE = 'social'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'social_django',
    'user',
]

SOCIAL_AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'project.urls'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': "losandreas",
    'API_KEY': "491482534251313",
    'API_SECRET': "8V1sHl0qcifmx_AB3DeExdlXJhg"
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())

