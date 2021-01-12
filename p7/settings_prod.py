from p7.settings_dev import *

DEBUG=False
ALLOWED_HOSTS = ['*']
# STATIC_ROOT = '/var/jobxprss_static'
MEDIA_ROOT = ''
AWS_ACCESS_KEY_ID = 'AKIA4EJCWTQ4QOSYSAWI'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'jobxprss-media'
AWS_LOG_BUCKET_NAME = 'jobxprss-log'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = 'us-east-2'

CLOUD_FRONT_ROOT_DOMAIN = 'd73v8sr570q51.cloudfront.net'
STATIC_URL = 'https://%s/' % (CLOUD_FRONT_ROOT_DOMAIN)
STATIC_BASE_URL_PREFIX = 'https://%s/' % (CLOUD_FRONT_ROOT_DOMAIN)
## AWS S3 bucket static file read code end
MEDIA_BUCKET_URL = 'jobxprss-media.s3.us-east-2.amazonaws.com'
MEDIA_BUCKET_URL_PREFIX = 'https://%s/' % (MEDIA_BUCKET_URL)

MEDIA_SOURCE = 'S3'
CLOUD_WATCH_LOG_GROUP = 'JobXprss'
CLOUD_WATCH_LOG_STREAM = 'jobxprss_api'

MEDIA_BUCKET_URL = 'jobxprss-media.s3.us-east-2.amazonaws.com'
MEDIA_URL = 'https://%s/' % (MEDIA_BUCKET_URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'p7_job',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
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
SITE_URL = 'https://jobxprss.com'

WEB_ACCESS_TOKEN_LIFETIME = timedelta(minutes=15)
WEB_REFRESH_TOKEN_LIFETIME = timedelta(days=1)
DEVICE_ACCESS_TOKEN_LIFETIME = timedelta(days=1)
DEVICE_REFRESH_TOKEN_LIFETIME = timedelta(days=30)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': WEB_ACCESS_TOKEN_LIFETIME,
    'REFRESH_TOKEN_LIFETIME': WEB_REFRESH_TOKEN_LIFETIME,
}

dev_mode = False

# PAYMENT_GATEWAY_URL = 'https://securepay.sslcommerz.com/gwprocess/v4/api.php'
# PAYMENT_VALIDATE_URL = 'https://securepay.sslcommerz.com/validator/api/validationserverAPI.php'
# PAYMENT_GATEWAY_STORE_ID = ''
# PAYMENT_GATEWAY_STORE_PASSWORD = ''
# IS_SANDBOX = False
