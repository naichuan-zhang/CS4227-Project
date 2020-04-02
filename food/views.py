from django.http import HttpResponse
from django.shortcuts import render
from .forms import FoodInputForm, adminCheckForm
from .foodfactory import *
from order.models import Item
from django.contrib import messages


def newFoodItem(request):
    if request.method == "POST":
        form = FoodInputForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            stock = form.cleaned_data['stock']
            price = form.cleaned_data['price']

            newfood = foodfactory.create_food(type,name,price,stock)
            newMenuItem = Item(name=newfood.getfoodname(),
                               type=newfood.getfoodtype(),
                               price=newfood.getfoodprice(),
                               stock=newfood.getfoodstock())
            newMenuItem.save()

    form = FoodInputForm()
    return render(request, 'main/food.html', {"form":form})


def adminCheck(request):
    form1 = FoodInputForm()
    form2 = adminCheckForm()
    if request.method == 'POST':
        form3 = adminCheckForm(request.POST)
        if form3.is_valid():
            password = form3.cleaned_data['password']
            username = form3.cleaned_data['username']
            if password == "123" and username == "admin":
                messages.success(request, "Successful Login")
                return render(request, 'main/food.html', {"form": form1})
            else:
                return render(request, 'main/adminCheck.html', {"form": form2})

    form4 = adminCheckForm()
    return render(request,'main/adminCheck.html', {"form": form4})