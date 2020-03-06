from django.urls import path

from App import views

name = 'app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='checkuser'),
    path('logout/', views.logout, name='logout'),
    path('me/', views.me, name='me'),
    path('sendemail/', views.send_email, name='sendemail'),
]
