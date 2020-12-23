import atexit
import io
import logging
import boto3
from django.conf import settings

# Internal Log Code Start
logging.basicConfig(
    filename=f'jobxprss_api.log',
    format='%(levelname)s [%(asctime)s]: %(message)s \nat %(funcName)s() in %(filename)s line %(lineno)s ',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
#
#
#
# def write_logs(body, bucket, key):
#     s3 = boto3.client("s3")
#     s3.put_object(Body=body, Bucket=bucket, Key=key)
#
#
# log = logging.getLogger("jobxprss")  ## Log file name
# log_stringio = io.StringIO()
# handler = logging.StreamHandler(log_stringio)
# log.addHandler(handler)
# atexit.register(write_logs, body=log_stringio.getvalue(), bucket=settings.AWS_LOG_BUCKET_NAME, key=settings.AWS_SECRET_ACCESS_KEY)
#
