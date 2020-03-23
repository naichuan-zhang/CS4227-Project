from collections import Counter

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from order.composite.itemcomposite import ItemComposite
from order.composite.itemleaf import ItemLeaf
from order.factory.discountfactory import DiscountFactory
from order.factory.orderitemfactory import OrderItemFactory
from order.memento.memento import Memento
from order.models import Item, Order, ItemTypeEnum, OrderStateEnum, Cart, OrderItem
from order.orderframework import OrderFramework
from user.models import User


def order(request):
    return render(request, 'main/order.html')


def create_order(request):

    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'order/create_order.html', context)


def view_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    context = {
        'orders': orders,
    }
    return render(request, 'order/view_orders.html', context)


def view_order(request):
    order_id = request.COOKIES['order_id']
    order = Order.objects.get(id=order_id)

    item_composite = ItemComposite()
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        order_i = ItemLeaf(item.item, item.amount)
        item_composite.add(order_i)

    user = request.user
    total_price = get_total_price(user, item_composite)
    discount_amount = item_composite.get_price() - total_price
    context = {
        'items': order_items,
        'total_price': total_price,
        'discount_amount': discount_amount,
    }
    return render(request, 'order/view_order.html', context)


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


# middleware is used to ensure user has logged in
def add_to_cart(request):
    itemId = request.GET.get('itemId')
    carts = Cart.objects.filter(item_id=itemId).filter(user=request.user)
    if carts.exists():
        cart_obj = carts.first()
        cart_obj.num = cart_obj.num + 1
    else:
        cart_obj = Cart()
        cart_obj.item_id = itemId
        cart_obj.user = request.user
    cart_obj.save()
    data = {
        'status': 200,
        'msg': "An item has been added to cart successfully!",
        'num': cart_obj.num,
    }
    return JsonResponse(data=data)


def remove_from_cart(request):
    itemId = request.GET.get('itemId')
    carts = Cart.objects.filter(item_id=itemId).filter(user=request.user)
    if carts.exists():
        cart_obj = carts.first()
        num = cart_obj.num - 1
        if num > 0:
            cart_obj.num = num
            cart_obj.save()
        else:
            cart_obj.delete()
    else:
        num = 0
    data = {
        'status': 200,
        'msg': "An item has been removed from cart successfully!",
        'num': num,
    }
    return JsonResponse(data=data)


def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    is_all_selected = cart_items.filter(is_selected=False).exists()
    item_composite = ItemComposite()
    for item in cart_items:
        item_leaf = ItemLeaf(item.item, item.num)
        item_composite.add(item_leaf)

    user = request.user
    total_price = get_total_price(user, item_composite)
    discount_amount = item_composite.get_price() - total_price
    context = {
        'title': 'My Cart',
        'carts': cart_items,
        'is_all_selected': is_all_selected,
        'total_price': round(total_price, 2),
        'discount_amount': round(discount_amount, 2),
    }
    return render(request, 'main/cart.html', context=context)


# TODO: part of checkout() method: for making an order
# make_order() func has been tested with Command DP.
def make_order(request):
    cart_items = Cart.objects.filter(is_selected=True).filter(user=request.user)
    item_composite = ItemComposite()
    for item in cart_items:
        item_leaf = ItemLeaf(item.item, item.num)
        item_composite.add(item_leaf)
        # delete all the items in Cart once order has been finished
        item.delete()

    framework = OrderFramework()
    # Command DP used here...
    user = request.user
    user_id = user.id
    total_price = get_total_price(user, item_composite)
    order_obj = framework.create_order(user_id=user_id, total_price=total_price)
    item_composite.create_order_item(order_obj)

    data = {
        'status': 200,
        'msg': 'ok',
        'order_id': order_obj.id,
    }
    return JsonResponse(data)


def get_total_price(user: User, item_composite: ItemComposite):
    orders = Order.objects.filter(user=user)
    discount_factory = DiscountFactory()
    discount = discount_factory.create_discount(orders.count())
    total_price = item_composite.get_price() * discount.get_discount()
    return total_price


def minus_item(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {
        'status': 200,
        'msg': 'ok',

    }
    original_num = cart.num
    memento = Memento(original_num)
    try:
        if cart.num > 1:
            cart.num = cart.num - 1
            cart.save()
            data['num'] = cart.num
            memento.save_state()
        else:
            cart.delete()
            data['num'] = 0
            memento.save_state()
    except:
        memento.restore_state(original_num)
        cart.num = original_num
        cart.save()
    data['total_price'] = Cart.get_total_price()

    return JsonResponse(data)


def plus_item(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {
        'status': 200,
        'msg': 'ok',
    }
    original_num = cart.num
    memento = Memento(original_num)
    try:
        cart.num = cart.num + 1
        cart.save()
    except:
        memento.restore_state(original_num)
        cart.num = original_num
        cart.save()
    data['num'] = cart.num
    data['total_price'] = Cart.get_total_price()

    return JsonResponse(data)

