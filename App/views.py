import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.constants import HTTP_USER_EXIST, HTTP_USER_OK
from App.email_helper import send_activate_email
from App.models import User
from App.userbuilder.userbuilder import UserBuilder
from App.userbuilder.userdirector import UserDirector
from CS4227_Project.settings import MEDIA_KEY_PREFIX


def home(request):
    return render(request, 'main/home.html')


def me(request):
    user_id = request.session.get('user_id')
    content = {
        "title": "Me",
        "is_login": False,
    }
    if user_id:
        user = User.objects.get(pk=user_id)
        content["is_login"] = True
        content["username"] = user.username
        content["icon"] = MEDIA_KEY_PREFIX + user.icon.url
    else:
        pass

    return render(request, 'main/me.html', content)


def register(request):
    if request.method == "GET":
        content = {
            "title": "Register",
        }
        return render(request, 'user/register.html', content)

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')

        # encode password
        password = make_password(password)

        # TODO: combine Builder with AbstractFactory??
        # use Builder Design Pattern to create an user
        user_director = UserDirector(UserBuilder())
        user = user_director.construct(username, password, email, icon)

        token = uuid.uuid4().hex
        cache.set(token, user.id, timeout=60*60*24)
        send_activate_email(username=username, receiver_email=email, token=token)

        return render(request, 'user/activate.html')


def login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        content = {
            "title": "Login",
        }
        if error_message:
            del request.session['error_message']
            content['error_message'] = error_message

        return render(request, 'user/login.html', content)

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if check_password(password, user.password):
                if user.is_active:
                    # save user into session
                    request.session['user_id'] = user.id
                    # redirect to Me when successful
                    return redirect(reverse('me'))
                else:
                    request.session['error_message'] = "Not activated yet"
                    return redirect(reverse('login'))
            else:
                request.session['error_message'] = "Wrong password"
                return redirect(reverse('login'))
        request.session['error_message'] = 'Username does not exist'
        return redirect(reverse('login'))


def check_user(request):
    """check if the username already exists or not when registration"""

    username = request.GET.get('username')
    users = User.objects.filter(username=username)
    data = {
        "status": HTTP_USER_OK,
        "msg": "Valid username",
    }
    if users.exists():
        data["status"] = HTTP_USER_EXIST
        data["msg"] = "Username already exists!"
    return JsonResponse(data=data)


def logout(request):
    request.session.flush()
    return redirect(reverse('me'))


def activate(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    if user_id:
        # allow user to activate email once only
        cache.delete(token)
        user = User.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        return redirect(reverse('login'))

    return render(request, 'user/activate_failed.html')
