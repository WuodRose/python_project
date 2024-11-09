from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+eg9g)#y2p^5oy*8(=mncv4*wsgnmhnos+-$y)oi0v^j1p62g0'

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',   # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static files handling

    'crispy_forms',
    'crispy_tailwind',
    'widget_tweaks',


    

    # My App 
    'Livestock_System',
]

# Add login URL and redirect
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session management
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication handling
    'django.contrib.messages.middleware.MessageMiddleware',  # Message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection

    


]

ROOT_URLCONF = 'Livestock_management.urls'

# TEMPLATES configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
            BASE_DIR / "Livestock_System" / "templates",  # Adjust path as necessary
        ],
        'APP_DIRS': True,  # Enable app-based templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debug info
                'django.template.context_processors.request',  # Request context
                'django.contrib.auth.context_processors.auth',  # User authentication context
                'django.contrib.messages.context_processors.messages',  # Messages context
            ],
        },
    },
]

WSGI_APPLICATION = 'Livestock_management.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MySQL database engine
        'NAME': 'Livestock_Management',  # Database name
        'USER': 'root',  # Database username
        'PASSWORD': 'Miccall.333',  # Database password (Change this for production!)
        'HOST': 'localhost',  # Database host (use IP address or domain in production)
        'PORT': '3306',  # MySQL default port
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # User attribute similarity check
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum length validation
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Common password validation
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Numeric password validation
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Language setting
TIME_ZONE = 'UTC'  # Time zone setting

USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable timezone-aware datetime objects

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'  # Static file URL path
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Define the location for your static files
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Output location for collectstatic

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Location where media files will be stored

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Use BigAutoField for primary keys

# Email backend (Optional)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Console email backend for dev purposes

# Caching (Optional, can be used to cache database queries or other data)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Simple in-memory cache for development
    }
}

