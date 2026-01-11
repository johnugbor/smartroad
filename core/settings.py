import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-key")

DEBUG = int(os.environ.get("DEBUG", 1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # 3rd Party Apps
    'rest_framework',
    'corsheaders',  # Required for React to talk to Django
    # 3rd Party
    'rest_framework.authtoken',

    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    
    # GeoDjango Framework
    'django.contrib.gis', 
    
    # Local Apps
    'users',
    'hazards',
]
SITE_ID = 1  # Required for allauth
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Must be before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]
# Point to our new model
AUTH_USER_MODEL = 'users.User'

# Allow login by Email OR Phone
AUTHENTICATION_BACKENDS = [
    'users.authentication.EmailOrPhoneBackend', # Our custom backend
    'django.contrib.auth.backends.ModelBackend', # Fallback
    'allauth.account.auth_backends.AuthenticationBackend', # Social Login
]
ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        # IMPORTANT: This engine enables PostGIS features
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('SQL_DATABASE', 'sraps_db'),
        'USER': os.environ.get('SQL_USER', 'sraps_user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'sraps_password'),
        'HOST': os.environ.get('SQL_HOST', 'db'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}

# JWT Settings
REST_auth = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'sraps-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'sraps-refresh-token',
    'REGISTER_SERIALIZER': 'dj_rest_auth.registration.serializers.RegisterSerializer',
}

# AllAuth Settings (Social Login)
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none' # Set to 'mandatory' in production


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# CORS SETTINGS (Crucial for React Frontend)
CORS_ALLOW_ALL_ORIGINS = True # Change this to specific domains in production