LOG_TO_AWS_CLOUD_WATCH = False

from p7.settings_prod import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME, CLOUD_WATCH_LOG_GROUP, \
    CLOUD_WATCH_LOG_STREAM
import logging
from cloudwatch import cloudwatch

format_string = '%(levelname)s [%(asctime)s] %(filename)s:%(lineno)s %(funcName)s %(message)s'
formatter = logging.Formatter(format_string)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dev_mode = False
if dev_mode:
    # File
    logging.basicConfig(filename=f'jobxprss_api.log', format=format_string,
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

if LOG_TO_AWS_CLOUD_WATCH:
    logger.setLevel(logging.WARNING)
    aws_handler = cloudwatch.CloudwatchHandler(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME,
                                               CLOUD_WATCH_LOG_GROUP, CLOUD_WATCH_LOG_STREAM)
    aws_handler.setFormatter(formatter)
    logger.addHandler(aws_handler)
