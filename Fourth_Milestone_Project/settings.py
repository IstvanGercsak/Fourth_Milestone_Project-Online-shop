"""
Django settings for Fourth_Milestone_Project project.

Generated by 'django-admin startproject' using Django 1.11.25.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
import dj_database_url

if os.path.exists('env.py'):
    import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# QA
if os.environ.get('QA'):
    development = False
    AWS_STORAGE_BUCKET_NAME = 'milestone-bucket-qa'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID_QA")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY_QA")
    print("Start Database on QA_branch")
    # DATABASE
    DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    # Static
    STATICFILES_LOCATION = "static"
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    # Media
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# PROD
elif os.environ.get('PROD'):
    development = False
    AWS_STORAGE_BUCKET_NAME = 'milestone-bucket-master'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID_MASTER")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY_MASTER")
    print("Start Database on PROD (master branch)")
    # DATABASE
    DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    # Static
    STATICFILES_LOCATION = "static"
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    # Media
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# local & DEV
else:
    # Set development to false in order to work the 404.html page
    development = True
    # DATABASE
    print("Start Database locally on DEV branch")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    # Static
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    # Media
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# AWS
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000'
}

AWS_STORAGE_BUCKET_NAME = "test"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = development

# ALLOWED_HOSTS = ['127.0.0.1',
#                  'online-shop-qa-branch.herokuapp.com',
#                  'last-milestone-online-shop.herokuapp.com']

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'storages.backends.s3boto3',
    'cart',
    'accounts',
    'products',
    'checkout',
    'blog',
    'home',
    'feed',
    'search'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Fourth_Milestone_Project.urls'

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
                # For images
                'django.template.context_processors.media',
                'cart.contexts.cart_contents'
            ],
        },
    },
]

WSGI_APPLICATION = 'Fourth_Milestone_Project.wsgi.application'

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

USE_L10N = True

USE_TZ = True

# Login with username or e-mail address
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth'
]

# Stripe
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Messages
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Kuld emailt-ha jo az email. Ha nem azonos vagy nem letezik, ellenorzes ra :(


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "istvan.gercsak@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv("GMAIL_PASSWORD")
