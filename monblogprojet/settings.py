from pathlib import Path
import os
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Sécurité
# -----------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-r*c-%i2on5x5(2mrm*k^@rx(y$qmrrg&%*=ldg2ro6-m3jgd-9')
DEBUG = False
ALLOWED_HOSTS = ['www.monblogamoi.com', 'monblogamoi.com'] 
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') 
SECRET_KEY=config('SECRET_KEY')
# -----------------------------
# Applications
# -----------------------------
INSTALLED_APPS = [
    'blogapp.apps.BlogappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Pour les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monblogprojet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'monblogprojet.wsgi.application'

# -----------------------------
# Base de données PostgreSQL
# -----------------------------

DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://dkjme17:KevapFwzzUzxBFWDL1bibTXCnPdj3G2T@dpg-d4qojq3e5dus73es4l40-a.virginia-postgres.render.com/postgress_3n5t',
        conn_max_age=600,
        ssl_require=True  # ⚠️ SSL obligatoire sur Render
    )
}


# -----------------------------
# Password validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -----------------------------
# Internationalisation
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Fichiers statiques
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------
# Authentification
# -----------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
