from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.constants import HTTP_USER_EXIST, HTTP_USER_OK
from App.models import User
from App.user_builder import GeneralUserWithoutIcon, GeneralUser
from CS4227_Project.settings import MEDIA_KEY_PREFIX, EMAIL_HOST_USER


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


def logout(request):
    request.session.flush()
    return redirect(reverse('me'))


# TODO: Failed !!!!!
# for testing send email operation
def send_email(request):
    subject = 'CS4227 Project | Activate your account'
    message = 'hello'
    from_email = EMAIL_HOST_USER
    recipient_list = ['zhangnaichuan168@gmail.com', ]
    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipient_list, fail_silently=False)
    return HttpResponse("send success")
