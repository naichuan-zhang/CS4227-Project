from django.shortcuts import render, redirect
from django.urls import reverse

from order.models import Item, Order


def order(request):
    return render(request, 'main/order.html')


def create_order(request):

    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'order/create_order.html', context)


def view_orders(request):

    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'order/view_orders.html', context)


# show food
def show_food(request):
    default_type = Item.get_types().first()
    return redirect(reverse('show_food_by_type', kwargs={
        'type': default_type
    }))


def show_food_by_type(request, type):
    items = Item.get_items_by_type(type)
    types = Item.get_types()
    context = {
        'items': items,
        'types': types,
    }
    return render(request, 'order/show.html', context=context)
