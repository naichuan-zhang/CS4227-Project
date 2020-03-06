import logging
import sys
from functools import wraps

filename = "./logging.log"
level = logging.DEBUG
logging.basicConfig(level=level, filename=filename, filemode='w+',
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def logger(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.info('%s.%s()' % (self.__class__.__name__, func.__name__))
        return func(*args, **kwargs)
    return wrapper
