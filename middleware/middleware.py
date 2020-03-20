from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User

LOGIN_LIST = [
    '/order/addtocart/',
    '/order/showcart/',
    '/order/makeorder/',
]


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path in LOGIN_LIST:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = User.objects.get(pk=user_id)
                    request.user = user
                except:
                    data = {
                        'status': 301,
                        'msg': 'User is not currently available!'
                    }
                    return JsonResponse(data=data)
            else:
                data = {
                    'status': 301,
                    'msg': 'Please login first!'
                }
                return JsonResponse(data=data)
