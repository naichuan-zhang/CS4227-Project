from django.urls import path

from food import views

urlpatterns = [
    path('show/', views.show, name='show'),
]
