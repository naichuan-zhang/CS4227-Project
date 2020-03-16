from foodfactory import *
from drinksfactory import *
from sides_factory import *


foodexample = foodfactory.create_food("Burger")
drinksexample = drinksfactory.create_drinks("Sprite")
sidesexample = sides_factory.create_sides("Chips")

print(foodexample.getfoodtype())
print(foodexample.getprice())
print(drinksexample.getdrinkstype())
print(drinksexample.getprice())
print(sidesexample.getsidestype())
print(sidesexample.getprice())


