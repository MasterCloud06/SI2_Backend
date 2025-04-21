import os
from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers
import dj_database_url

# ─────────────────────────────────────
# BASE CONFIG
# ─────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Usar variable de entorno para producción
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-i&@!wo*^e7ioyuf#^ei^lix&u2+dh(_qs2s*t&1wxw3d^8^woi')

# DEBUG: Desactivado en producción
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

# ALLOWED_HOSTS: Configurado para Render
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.onrender.com,localhost,127.0.0.1').split(',')

# ─────────────────────────────────────
# INSTALLED APPS
# ─────────────────────────────────────
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'corsheaders',
    'rest_framework',
    'django_filters',
    'whitenoise.runserver_nostatic',

    # Apps propias
    'apps.auth_app',
    'apps.usuarios',
    'apps.productos',
    'apps.ventas',
    'apps.reportes',
    'apps.contabilidad',
    'apps.crm',
    'apps.voz',
    'apps.categoria',
    'apps.pagos',
    'apps.recomendaciones',
    'apps.notificaciones',
    'apps.carrito',
]

# ─────────────────────────────────────
# MIDDLEWARE
# ─────────────────────────────────────
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ─────────────────────────────────────
# URLS / TEMPLATES / WSGI
# ─────────────────────────────────────
ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# ─────────────────────────────────────
# DATABASE - Configurado para Render
# ─────────────────────────────────────
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# ─────────────────────────────────────
# AUTH
# ─────────────────────────────────────
AUTH_USER_MODEL = 'usuarios.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# ─────────────────────────────────────
# PASSWORD VALIDATION
# ─────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─────────────────────────────────────
# INTERNATIONALIZATION
# ─────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ─────────────────────────────────────
# STATIC FILES
# ─────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de Whitenoise para servir archivos estáticos comprimidos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─────────────────────────────────────
# REST FRAMEWORK
# ─────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS': None,
    'PAGE_SIZE': None,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# ─────────────────────────────────────
# CORS CONFIG
# ─────────────────────────────────────
CORS_ALLOW_CREDENTIALS = True

# Permitir todos los orígenes en producción (más seguro es especificar orígenes)
CORS_ALLOW_ALL_ORIGINS = True

# O especificar orígenes permitidos:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "http://localhost:5174",
#     "https://famous-cuchufli-d9d4b1.netlify.app",
#     # Añadir más orígenes si es necesario
# ]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-CSRFToken',
    'Authorization',
    'Content-Type',
]

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
    "https://famous-cuchufli-d9d4b1.netlify.app",
    "http://localhost:5173",
    "http://localhost:5174",
]

# ─────────────────────────────────────
# STRIPE
# ─────────────────────────────────────
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")

# ─────────────────────────────────────
# SIMPLE JWT
# ─────────────────────────────────────
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ─────────────────────────────────────
# LOGGING (para depuración)
# ─────────────────────────────────────
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}