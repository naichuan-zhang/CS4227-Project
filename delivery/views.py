from django.shortcuts import render

from order.models import Order, OrderItem

def delivery(request):

        user = request.user
        orders = Order.objects.filter(user=user)
        context = {
            'orders': orders,
        }
        return render(request, 'delivery/delivery.html', context)

def view_delivery(request):
        order_id = request.COOKIES['order_id']
        order = Order.objects.get(id=order_id)
        delivery_states = ["in preperation", "available for delivery", "out for delivery", "delivered"]
        button_states1 = ["in preperation", "edit order", "cancel delivery", "delivered"]
        button_states2 = ["make ready for delivery", "send for delivery", "complete delivery", "delivered"]
        count = 0
        delivery_state = delivery_states[count]
        button_state1 = button_states1[count]
        button_state2 = button_states2[count]
        order_items = OrderItem.objects.filter(order=order)



        context = {
                'items': order_items,
                'delivery_state': delivery_state,
                'button_state1': button_state1,
                'button_state2': button_state2
        }

        return render(request, 'delivery/view_delivery.html', context)