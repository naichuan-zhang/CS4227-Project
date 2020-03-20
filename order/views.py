from collections import Counter

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from order.composite.itemcomposite import ItemComposite
from order.composite.itemleaf import ItemLeaf
from order.factory.orderitemfactory import OrderItemFactory
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


def show_cart(request):
    carts = Cart.objects.filter(user=request.user)
    is_all_selected = carts.filter(is_selected=False).exists()
    total_price = Cart.get_total_price()
    context = {
        'title': 'My Cart',
        'carts': carts,
        'is_all_selected': is_all_selected,
        'total_price': total_price,
    }
    return render(request, 'main/cart.html', context=context)


# TODO: part of checkout() method: for making an order
# make_order() func has been tested with Command DP.
def make_order(request):
    carts = Cart.objects.filter(is_selected=True).filter(user=request.user)
    framework = OrderFramework()
    # Command DP used here...
    user_id = request.user.id
    total_price = Cart.get_total_price()
    order_obj = framework.create_order(user_id=user_id, total_price=total_price)
    for cart in carts:
        orderitem = OrderItem()
        orderitem.order = order_obj
        orderitem.item = cart.item
        orderitem.amount = cart.num
        orderitem.save()
        # delete all the items in Cart once order has been finished
        cart.delete()
    data = {
        'status': 200,
        'msg': 'ok',
        'order_id': order_obj.id,
    }
    return JsonResponse(data)


# def checkout(request):
#     if request.method == 'POST':
#         addr = request.POST['address']
#         ordid = request.POST['oid']
#         Order.objects.filter(id=int(ordid)).update(delivery_addr=addr, state=Order.ORDER_STATE_PLACED)
#         return redirect('/orderplaced/')
#     else:
#         user_id = request.session.get('user_id')
#         user = User.objects.get(id=user_id)
#         try:
#             order = Order.objects.get(user=user, state=OrderStateEnum.PENDING)
#         except Order.DoesNotExist:
#             order = Order(user=user)
#             order.save()
#
#         cart = request.COOKIES['cart'].split(",")
#         cart = dict(Counter(cart))
#
#         item_composite = ItemComposite("Order")
#         main_composite = ItemComposite("Mains")
#         side_composite = ItemComposite("Sides")
#         drink_composite = ItemComposite("Drinks")
#         # factory = OrderItemFactory()
#
#         list = []
#         for i, c in cart.items():
#             item = Item.objects.get(id=int(i))
#             list.append(len(item.type))
#             if item:
#                 # factory.create_order_item(item, order, c)
#
#                 if item.type == 'MAIN':
#                     main_composite.add(ItemLeaf(item, c))
#                 elif item.type == 'SIDE':
#                     side_composite.add(ItemLeaf(item, c))
#                 else:
#                     drink_composite.add(ItemLeaf(item, c))
#
#         item_composite.add(main_composite)
#         item_composite.add(side_composite)
#         item_composite.add(drink_composite)
#
#         context = {
#             "composite": item_composite,
#             "list": list,
#         }
#
#         return render(request, 'order/checkout.html', context)
