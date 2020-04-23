from django.urls import path

from delivery import views

urlpatterns = [
    path('delivery/', views.delivery, name='delivery'),
    path('view_delivery', views.view_delivery, name='view_delivery'),
]