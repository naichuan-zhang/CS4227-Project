from django.urls import path

from order import views

urlpatterns = [
    path('', views.order, name='order'),
    path('create/', views.create_order, name='create_order'),
    path('previous/', views.view_orders, name='view_orders'),
]
