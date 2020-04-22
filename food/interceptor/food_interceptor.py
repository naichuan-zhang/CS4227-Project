from .Context import *
from logger import *
import re

class food_interceptor:

    def on_log_event(self,context):

       pattern = re.compile(r'[a-zA-z]\s+')
       data = context.get_name()

       if(re.search(pattern, data)):
            nothing = None
       else:
           logging.info('Invalid format for new menu item entered : ' + data)






