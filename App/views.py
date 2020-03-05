from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.constants import HTTP_USER_EXIST, HTTP_USER_OK
from App.models import User


def home(request):
    return render(request, 'main/home.html')


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

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.icon = icon

        user.save()
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
        # TODO: query
        return HttpResponse("LOGIN SUCCESS!!!")


def check_user(request):
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
