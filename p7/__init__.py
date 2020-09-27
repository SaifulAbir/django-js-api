import logging

logging.basicConfig(
    filename=f'jobxprss-api.log',
    format='%(levelname)s [%(asctime)s]: %(message)s \nat %(funcName)s() in %(filename)s line %(lineno)s ',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)