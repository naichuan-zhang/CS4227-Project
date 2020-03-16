class Drink(object):
    price = ""
    drinkstype = ""

    def getprice(self):
        return self.price

    def getdrinkstype(self):
        return self.drinkstype

class CocaCola(Drink):
    drinkstype = "Coca-Cola"
    price = "2.50"

class Sprite(Drink):
    drinkstype = "Sprite"
    price = "2.60"

class Fanta(Drink):
    drinkstype = "Fanta"
    price = "2.80"

class ClubOrange(Drink):
    drinkstype = "Club Orange"
    price = "2.30"

class Water(Drink):
    drinkstype = "Water"
    price = "1.50"

class drinksfactory(object):
    @classmethod
    def create_drinks(self, drinkstype):
        targetclass = drinkstype.capitalize()
        return globals()[targetclass]()








