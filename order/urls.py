from django.urls import path

from order import views

urlpatterns = [
    path('show/', views.show, name='show'),
]
