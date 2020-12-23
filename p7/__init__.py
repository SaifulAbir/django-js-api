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
else:
    # TODO read from prod setting
    aws_handler = cloudwatch.CloudwatchHandler('AKIA4EJCWTQ4QOSYSAWI', 'a9b3YULZNFxYkg0HvcTIGyUfANIbsSRVmeiTIpKW', 'us-east-2', 'JobXprss',
                                               'jobxprss_api')
    aws_handler.setFormatter(formatter)
    logger.addHandler(aws_handler)
