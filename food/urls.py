from django.urls import path

from food import views

urlpatterns = [
    path('', views.newFoodItem, name='food'),
    path('adminCheck/',views.adminCheck,name ='adminCheck')
]
