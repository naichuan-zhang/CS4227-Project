from collections import Counter

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from order.forms import PaymentForm, CardForm
from order.composite.itemcomposite import ItemComposite
from order.composite.itemleaf import ItemLeaf
from order.factory.discountfactory import DiscountFactory
from order.factory.orderitemfactory import OrderItemFactory
from order.memento.caretaker import Caretaker
from order.memento.memento import Memento
from order.memento.originator import Originator
from order.models import Item, Order, ItemTypeEnum, OrderStateEnum, Cart, OrderItem
from order.orderframework import OrderFramework
from order.strategy.paypaypal import PayPaypal
from order.strategy.strategy import Strategy
from order.strategy.paycontext import Context
from order.visitor.stringvisitor import StringVisitor
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

    if request.method == "POST" and 'paypal1' in request.POST:
        form = PaymentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            context = Context(PayPaypal())
            context.pay(email,password)
    else:
        form = PaymentForm()

    item_composite = ItemComposite()
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        order_i = ItemLeaf(item.item, item.amount)
        item_composite.add(order_i)

    user = request.user
    total_price = get_total_price(user, item_composite)
    discount_amount = item_composite.get_price() - total_price
    context = {
        'form': form,
        'items': order_items,
        'total_price': round(total_price, 2),
        'discount_amount': round(discount_amount, 2),
    }
    return render(request, 'order/view_order.html', context)


def paycard(request):

    if request.method == "POST" and 'card1' in request.POST:
        form1 = CardForm(request.POST)
        if form1.is_valid():
            name = form1.cleaned_data['name']
            number = form1.cleaned_data['number']
            print(name + number)

    form1 = CardForm()
    context = form1

    return render(request, 'order/paymentcomp.html', context)

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
    carts = Cart.objects.filter(user=request.user)
    is_all_selected = carts.filter(is_selected=False).exists()
    item_composite = ItemComposite()
    for item in carts:
        item_leaf = ItemLeaf(item.item, item.num)
        item_composite.add(item_leaf)

    user = request.user
    total_price = get_total_price(user, item_composite)
    discount_amount = item_composite.get_price() - total_price
    context = {
        'title': 'My Cart',
        'carts': carts,
        'is_all_selected': is_all_selected,
        'total_price': round(total_price, 2),
        'discount_amount': round(discount_amount, 2),
    }
    return render(request, 'main/cart.html', context=context)


# TODO: Implement Payment
# make_order() func has been tested with Command DP.
def make_order(request):
    carts = Cart.objects.filter(is_selected=True).filter(user=request.user)
    if carts:
        item_composite = ItemComposite()
        for item in carts:
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
    total_price = item_composite.get_price() * discount.get_multiplier()
    return total_price


def minus_item(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {
        'status': 200,
        'msg': 'ok',

    }
    original_num = cart.num
    # use Memento DP to handle exceptions
    originator = Originator(state=original_num)
    caretaker = Caretaker(originator=originator)
    try:
        if cart.num > 1:
            cart.num = cart.num - 1
            cart.save()
            data['num'] = cart.num
            # save the current cart.num
            originator.set_state(state=cart.num)
            caretaker.save()
        else:
            cart.delete()
            data['num'] = 0
            # save the current cart.num
            originator.set_state(state=cart.num)
            caretaker.save()
    except:
        # rollback to original_num when error occurs
        caretaker.undo()
        cart.num = originator.get_state()
        cart.save()

    user = request.user
    carts = Cart.objects.filter(is_selected=True).filter(user=user)
    item_composite = ItemComposite()
    for item in carts:
        item_leaf = ItemLeaf(item.item, item.num)
        item_composite.add(item_leaf)
    total_price = get_total_price(user, item_composite)
    data['total_price'] = round(total_price, 2)
    data['discount'] = round(item_composite.get_price() - total_price, 2)

    return JsonResponse(data)


def plus_item(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {
        'status': 200,
        'msg': 'ok',
    }
    original_num = cart.num
    # use Memento DP to handle exceptions
    originator = Originator(state=original_num)
    caretaker = Caretaker(originator=originator)
    try:
        cart.num = cart.num + 1
        # save the current cart.num
        originator.set_state(state=cart.num)
        caretaker.save()
        cart.save()
    except:
        # rollback to original_num when error occurs
        caretaker.undo()
        cart.num = originator.get_state()
        cart.save()
    data['num'] = cart.num

    user = request.user
    carts = Cart.objects.filter(is_selected=True).filter(user=user)
    item_composite = ItemComposite()
    for item in carts:
        item_leaf = ItemLeaf(item.item, item.num)
        item_composite.add(item_leaf)
    total_price = get_total_price(user, item_composite)
    data['total_price'] = round(total_price, 2)
    data['discount'] = round(item_composite.get_price() - total_price, 2)

    return JsonResponse(data)


def show_data(request):
    data = []
    visitor = StringVisitor()
    orders = Order.objects.all()
    carts = Cart.objects.all()
    items = Item.objects.all()

    for o in orders:
        data.append(o.accept(visitor))
    for c in carts:
        data.append(c.accept(visitor))
    for i in items:
        data.append(i.accept(visitor))

    context = {
        'data': data,
    }

    return render(request, 'order/data.html', context=context)

