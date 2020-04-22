from .Context import *
from .food_dispatcher import *

class InterceptorFramework:

    foodDispatcher = food_dispatcher()

    def __init__(self):
        self.foodDispatcher = food_dispatcher()

    def register_food_interceptor(self,interceptor):

        return self.foodDispatcher.register_food_interceptor(interceptor)

    def remove_food_interceptor(self,interceptor):

        return self.foodDispatcher.remove_food_interceptor(interceptor)

    def on_log_event(self,context):

        self.foodDispatcher.on_log_event(context)







