from django.urls import path

from App import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
