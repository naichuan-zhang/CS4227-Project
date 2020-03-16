class Food(object) :
    price = ""
    foodtype = ""

    def getprice(self):
        return self.price

    def getfoodtype(self):
        return self.foodtype

class Burger(Food) :
    foodtype = "Burger"
    price = "5.00"

class Kebab(Food) :
    foodtype = "Kebab"
    price = "5.00"

class Pizza(Food) :
   foodtype = "Pizza"
   price = "8.00"

class ChickenBurger(Food) :
   foodtype = "Chicken Burger"
   price = "5.00"

class ChickenWrap(Food) :
   foodtype = "Chicken Wrap"
   price = "6.00"

class foodfactory(object):
    @classmethod
    def create_food(self,foodtype):
        targetclass = foodtype.capitalize()
        return globals()[targetclass]()

        






