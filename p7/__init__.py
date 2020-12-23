from django.conf import settings
import logging
from cloudwatch import cloudwatch

format_string = '%(levelname)s [%(asctime)s] %(filename)s:%(lineno)s %(funcName)s %(message)s'
formatter = logging.Formatter(format_string)
logger = logging.getLogger()

# File
logging.basicConfig(filename=f'jobxprss_api.log', format=format_string,
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)


if not settings.dev_mode:
    logger.setLevel(logging.WARNING)
    aws_handler = cloudwatch.CloudwatchHandler(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, settings.AWS_S3_REGION_NAME, settings.AWS_SECRET_ACCESS_KEY,
                                               settings.CLOUD_WATCH_LOG_GROUP, settings.CLOUD_WATCH_LOG_STREAM)
    aws_handler.setFormatter(formatter)
    logger.addHandler(aws_handler)
