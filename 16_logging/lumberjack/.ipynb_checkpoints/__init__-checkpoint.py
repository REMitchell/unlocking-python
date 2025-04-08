import logging
import sys

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG, handlers=[stream_handler])


# format_str = '%(levelname)s:%(asctime)s:%(message)s'
'''
logging.basicConfig(
    level=logging.DEBUG,
    format=format_str,
    datefmt='%m/%d/%Y %H:%M:%S'
)
'''
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S'
)


file_handler = logging.FileHandler('lumberjack.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

logger.debug('Importing package')
