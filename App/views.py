from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.constants import HTTP_USER_EXIST, HTTP_USER_OK
from App.models import User
from App.user_builder import GeneralUserWithoutIcon, GeneralUser


def home(request):
    return render(request, 'main/home.html')


def me(request):
    user_id = request.session.get('user_id')
    content = {
        "title": "Me",
    }
    if user_id:
        pass
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

        # use Builder Design Pattern to create an user
        user = GeneralUser()
        user.construct(username, password, email, icon)

        return redirect(reverse('login'))


def login(request):
    if request.method == "GET":
        content = {
            "title": "Login",
        }
        return render(request, 'user/login.html', content)

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if check_password(password, user.password):
                # save user into session
                request.session['user_id'] = user.id
                # redirect to Me when successful
                return redirect(reverse('me'))
            else:
                return redirect(reverse('login'))
        print("Invalid username or password!!!")
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
