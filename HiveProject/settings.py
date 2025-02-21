from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# # Session will expire when the user closes the browser
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# # Set session timeout (in seconds)
# SESSION_COOKIE_AGE = 300  # 5 minutes (or customize as needed)

# # Ensure cookies are only sent over HTTPS
# SESSION_COOKIE_SECURE = True  # Use in production with HTTPS enabled  PS
SESSION_COOKIE_HTTPONLY = True

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'channels',
    'Mainapp',
    'Accounts',
    'DashboardPages',
    'Teamworkspace',
    'TeamworkspaceChat',
    'TalentMatching',
    'tailwind',
    'theme',
    'django_browser_reload',
    'EmployersDashboard',
    'cities_light',
    'UserProfile',
    
    
]

# Login URL Configuration
LOGIN_URL = 'accounts:Login'
LOGOUT_REDIRECT_URL = 'accounts:Login'
LOGIN_REDIRECT_URL = 'dashboard:job_view'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Accounts.middleware.AdminRedirectMiddleware',  
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


# COMPRESS_ROOT = BASE_DIR / 'static'

# COMPRESS_ENABLED = True

# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)



ROOT_URLCONF = 'HiveProject.urls'

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
ASGI_APPLICATION = 'HiveProject.asgi.application'

WSGI_APPLICATION = 'HiveProject.wsgi.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
         'OPTIONS': {
            'timeout': 20,  
        },
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'False') == 'False'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your_email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your_app_password')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'your_email@gmail.com')

# Cache configuration for OTP storage
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Session configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
