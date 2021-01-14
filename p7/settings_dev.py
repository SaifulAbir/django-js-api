"""
Django settings for p7 project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pg%n(up#+36@3*g)dyo7z6)o73ybdv0%zgjbig*9xd@z+bbk*1'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS=['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_reorder',
    'job',
    'messaging',
    'rest_framework',
    'pro',
    'django_rest_passwordreset',
    'rest_framework.authtoken',
    'django_admin_listfilter_dropdown',
    'ckeditor',
    'mathfilters',
    'testimonial',
    'settings',
    'career_advice',
    'django_user_agents',
     'rangefilter',
    'django_bot_crawler_blocker',
    'feedback',
    'storages',
    'account',
]

MIDDLEWARE = [
    'p7.crawler_blocker.P7CrawlerBlockerMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]


USER_AGENTS_CACHE = 'default'

ROOT_URLCONF = 'p7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'p7.context_processors.footer_context',
            ],
        },
    },
]

## Django crawler
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

MAX_ALLOWED_HITS_PER_IP = 100000
IP_HITS_TIMEOUT=60



WSGI_APPLICATION = 'p7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p7',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
            'isolation_level': "repeatable read",
        },
        'CHARSET':'utf8',
        'COLLATION':'utf8_general_ci',
        'COLLATION_CONNECTION':'utf8_general_ci'
    }
}


CORS_ORIGIN_ALLOW_ALL = True
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'p7.validators.ResetPasswordValidator',
    }

]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'p7.auth.P7Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'p7.permissions.P7Permission',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'p7.pagination.P7Pagination',
    # 'PAGE_SIZE': 10
}

WEB_ACCESS_TOKEN_LIFETIME = timedelta(minutes=15)
WEB_REFRESH_TOKEN_LIFETIME = timedelta(days=1)
DEVICE_ACCESS_TOKEN_LIFETIME = timedelta(days=1)
DEVICE_REFRESH_TOKEN_LIFETIME = timedelta(days=30)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': WEB_ACCESS_TOKEN_LIFETIME,
    'REFRESH_TOKEN_LIFETIME': WEB_REFRESH_TOKEN_LIFETIME,
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd-m-Y'
DATE_INPUT_FORMATS = [
    '%d-%m-%Y',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

## Only for local
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 6000
SITE_URL = 'http://localhost'
SOCKET_BASE_URL = "https://iss.ishraak.com:443"
SOCKET_SERVER_TOKEN = "xNTk3ODk0ODE5LCJqdGkiOiJiMGYxODEyOWI0Mjk0OGU4YmFjMmQwMWRmNDdlNTM0YyIsInVzZXJfaWQiOjUwfQ"
SOCKET_MAX_THREAD = 5
APP_VERSION_NUMBER = 'v1.0.86'
## ToDo Shohag news_dev for testing news for production
FIREBASE_CLOUD_MESSAGING_TOPIC = 'news'



# GOOGLE_MAPS_API_KEY = 'AIzaSyCRDW0MU2nUZMZGryae1hb8oJEG6Cr_oLQ'
GOOGLE_MAPS_API_KEY = 'AIzaSyBYT7cwP2Ki9fwJBmRH6t2FkjjkjsywVaE'

CKEDITOR_CONFIGS = {
   'default': {
       'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList'],
            ['Indent','Outdent'],
            ['Link', 'Unlink'],
            ['Source'],
       ]
   }
}

WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'

WKHTMLTOPDF_CMD_OPTIONS = {
'quiet': True,
}

ADMIN_REORDER = (
    {
        'app': 'job', 'label': 'Companies and Jobs',
        'models': (
            'job.Company',
            'job.Job',
            'job.JobApplication',
            'job.TrendingKeywords',
        )
    },
    {
        'app': 'messaging', 'label': 'Messaging',
        'models': (
            'messaging.EmployerMessage',
            'messaging.Notification',
            'messaging.FcmCloudMessaging',
        )
    },
    {
        'app': 'pro', 'label': 'Professionals',
        'models': (
            'pro.Professional',
            'pro.Certification',
            'pro.Membership',
            'pro.Portfolio',
            'pro.ProfessionalEducation',
            'pro.ProfessionalSkill',
            'pro.Reference',
            'pro.WorkExperience',
        )
    },
    {
        'app': 'auth', 'label': 'Users and Groups',
        'models': (
            'auth.User',
            'auth.Group',
        )
    },
    {
        'app': 'job', 'label': 'Setups',
        'models': (
            'job.ApplicationStatus',
            'job.City',
            'job.Currency',
            'job.Experience',
            'job.JobGender',
            'job.Gender',
            'job.Industry',
            'job.JobCategory',
            'job.JobSource',
            'job.Qualification',
            'job.Skill',
            'job.JobRecommendation'
        )
    },
    {
        'app': 'pro', 'label': 'Setups (Pro)',
        'models': (
            'pro.CertifyingOrganization',
            'pro.CertificateName',
            'pro.EducationLevel',
            'pro.Institute',
            'pro.Major',
            'pro.MembershipOrganization',
            'pro.Nationality',
            'pro.Organization',
            'pro.Religion',
        )
    },
    {
        'app': 'settings', 'label': 'System Settings',
        'models': (
            'settings.Settings',
        )
    },
    {
        'app': 'career_advice', 'label': 'Career Advice',
        'models': (
            'career_advice.CareerAdvice',
        )
    },
    {
        'app': 'testimonial', 'label': 'Testimonial',
        'models': (
            'testimonial.Testimonial',
        )
    },
)

# For production MEDIA_SOURCE = 'S3'
MEDIA_SOURCE = 'Local'
dev_mode = True
PAYMENT_GATEWAY_URL = 'https://sandbox.sslcommerz.com/gwprocess/v4/api.php'
PAYMENT_VALIDATE_URL = 'https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php'
PAYMENT_GATEWAY_STORE_ID = 'jobxp5fcdcfa69d176'
PAYMENT_GATEWAY_STORE_PASSWORD = 'jobxp5fcdcfa69d176@ssl'
IS_SANDBOX = True
CEREAR_ADVICE_THUMBNAIL_DEFAULT_IMAGE_WIDTH = 200
CEREAR_ADVICE_FEATURED_DEFAULT_IMAGE_WIDTH = 500
MEDIA_BUCKET_URL_PREFIX = "http://localhost/"
STATIC_BASE_URL_PREFIX = "http://localhost/"