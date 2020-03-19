from django.urls import path

from order import views

urlpatterns = [
    path('', views.order, name='order'),
    path('create/', views.create_order, name='create_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('previous/', views.view_orders, name='view_orders'),
    path('show/', views.show_food, name='show_food'),
    path('showbytype/<str:type>', views.show_food_by_type, name='show_food_by_type'),
    path('addtoorder/', views.add_to_order, name='add_to_order'),
]
