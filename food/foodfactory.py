class Food(object):
    id = ""
    name = ""
    price = ""
    type = ""
    stock = ""

    def getfoodprice(self):
        return self.price

    def getfoodtype(self):
        return self.type

    def getfoodid(self):
        return self.id

    def getfoodstock(self):
        return self.stock

    def getfoodname(self):
        return self.name

class Starter(Food):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.type = "STARTER"
        self.stock = stock

class Main(Food):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.type = "MAIN"
        self.stock = stock


class Desert(Food):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.type = "DESSERT"
        self.stock = stock


class Drink(Food):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.type = "DRINK"
        self.stock = stock

class foodfactory():

    def create_food(type, name, price, stock):
        if type == "Starter":
            return Starter(name, price, stock)
        elif type == "Main":
            return Main(name, price, stock)
        elif type == "Dessert":
            return Desert(name, price, stock)
        elif type == "Drink":
            return Drink(name, price, stock)
        else:
            return None


