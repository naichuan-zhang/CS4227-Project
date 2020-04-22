from .Context import *

class food_dispatcher:

    interceptor_list = []

    def register_food_interceptor(self,interceptor):

        return self.interceptor_list.append(interceptor)

    def remove_food_interceptor(self,interceptor):

        return self.interceptor_list.remove(interceptor)

    def on_log_event(self,context):

        for x in self.interceptor_list:
            x.on_log_event(context)
