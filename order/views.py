from django.http import HttpResponse
from django.shortcuts import render


def order(request):
    return render(request, 'main/order.html')


def create_order(request):
    return render(request, 'order/create_order.html')


def view_orders(request):
    return render(request, 'order/view_orders.html')
