from django.urls import path

from order import views

urlpatterns = [
    path('', views.order, name='order'),
    path('create/', views.create_order, name='create_order'),
    path('previous/', views.view_orders, name='view_orders'),
    path('previous/view/', views.view_order, name='view_order'),
    path('show/', views.show_food, name='show_food'),
    path('showbytype/<str:type>', views.show_food_by_type, name='show_food_by_type'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('removefromcart/', views.remove_from_cart, name='remove_from_cart'),
    path('showcart/', views.show_cart, name='show_cart'),
    path('makeorder/', views.make_order, name='make_order'),
    path('minusitem/', views.minus_item, name='minus_item'),
    path('plusitem/', views.plus_item, name='plus_item'),
    path('data/', views.show_data, name='show_data'),
    path('previous/view/make_payment', views.make_payment, name='make_payment'),
]
