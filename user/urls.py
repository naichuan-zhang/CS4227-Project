from django.urls import path

from user import views

name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='checkuser'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.me, name='me'),
    path('activate/', views.activate, name='activate'),
]
