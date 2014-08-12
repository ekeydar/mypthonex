import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s',convertor=time.gmtime)
logging.warning('is when this event was logged.')

