import os
from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers
import dj_database_url # Importamos dj_database_url
# from dotenv import load_dotenv # Opcional: descomentar si usas python-dotenv localmente

# Cargar variables de entorno desde un archivo .env si existe (opcional, para desarrollo local)
# load_dotenv()

# ─────────────────────────────────────
# BASE CONFIG
# ─────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Usar variable de entorno para producción
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-i&@!wo*^e7ioyuf#^ei^lix&u2+dh(_qs2s*t&1wxw3d^8^woi') # <- Clave por defecto solo para desarrollo local si no hay .env

# DEBUG: Usar variable de entorno, asegurando que sea False en producción
DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1')

# ALLOWED_HOSTS: Usar variable de entorno para producción
# Render añadirá su dominio aquí. En Render, configuras ALLOWED_HOSTS como el dominio de tu app (ej: your-app-name.onrender.com)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
# Si quieres mantener los hosts locales para desarrollo, puedes combinarlos:
# LOCAL_ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ','.join(LOCAL_ALLOWED_HOSTS)).split(',')


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
    'whitenoise.runserver_nostatic', # Agregamos whitenoise para servir estáticos en producción
    'whitenoise',

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
    'corsheaders.middleware.CorsMiddleware',  # ← Importante que esté primero
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Agregamos whitenoise middleware justo después de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Asegúrate de tener este si necesitas protección CSRF
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
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ─────────────────────────────────────
# DATABASE
# ─────────────────────────────────────
# Configuración para PostgreSQL usando dj_database_url y la variable de entorno DATABASE_URL de Render
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600 # Opcional: Configura la edad máxima de conexión en segundos
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
# STATIC_ROOT es donde collectstatic reunirá todos los archivos estáticos para producción
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración de Whitenoise para servir archivos estáticos comprimidos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Opcional: Configuración para archivos media subidos por usuarios (si los tienes)
# En Render Free, necesitarás almacenamiento externo para esto (AWS S3, Cloudinary, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles') # Directorio local para media


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─────────────────────────────────────
# REST FRAMEWORK
# ─────────────────────────────────────
REST_FRAMEWORK = {
    # Sólo JWTAuthentication (no SessionAuthentication → no chequeo CSRF)
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
# En producción, deberías configurar esto usando variables de entorno en Render
# CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:5173,http://localhost:5174').split(',')
# O podrías permitir todos los orígenes en producción si es una API pública, aunque no es lo más seguro:
# CORS_ALLOW_ALL_ORIGINS = not DEBUG # Permite todos los orígenes si DEBUG es False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    # Agrega aquí la URL de tu frontend en producción cuando la tengas
    # os.environ.get('FRONTEND_URL_RENDER'), # Ejemplo si la guardas en una variable de entorno
]

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

# CSRF_TRUSTED_ORIGINS: También considera usar variables de entorno en producción
# CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', 'http://localhost:5173,http://localhost:5174').split(',')
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
     # Agrega aquí la URL de tu frontend en producción cuando la tengas
    # os.environ.get('FRONTEND_URL_RENDER'), # Ejemplo si la guardas en una variable de entorno
]


# ─────────────────────────────────────
# OTRAS KEYS (por ejemplo Stripe)
# ─────────────────────────────────────
# Ya estás usando os.getenv, lo cual es correcto para variables de entorno
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
    # Considera usar un signing key diferente para producción guardado en variables de entorno
    # 'SIGNING_KEY': os.environ.get('SIMPLE_JWT_SIGNING_KEY', settings.SECRET_KEY),
}