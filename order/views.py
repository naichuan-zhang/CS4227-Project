from django.http import HttpResponse
from django.shortcuts import render

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
