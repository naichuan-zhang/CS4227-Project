class Context(object):
    name = ""
    type = ""
    stock = ""
    price = ""

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_stock(self):
        return self.stock

    def get_price(self):
        return self.price

class NewMenuItemContext(Context):

    name = ""
    type = ""
    stock = ""
    price = ""

    def __init__(self,name,type,stock,price):

        self.name = name
        self.type = type
        self.stock = stock
        self.price = price









