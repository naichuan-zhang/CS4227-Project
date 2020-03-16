class Sides(object):
    price = ""
    sidestype = ""

    def getprice(self):
        return self.price

    def getsidestype(self):
        return self.sidestype

class Chips(Sides):
    sidestype = "Chips"
    price = "2.50"

class Wedges(Sides):
    sidestype = "Wedges"
    price = "2.90"

class Salad(Sides):
    sidestype = "Salad"
    price = "1.80"

class OnionRings(Sides):
    sidestype = "Onion Rings"
    price = "3.20"

class GarlicBread(Sides):
    sidestype = "Garlic Bread"
    price = "3.50"

class sides_factory(object):
    @classmethod
    def create_sides(self, sidestype):
        targetclass = sidestype.capitalize()
        return globals()[targetclass]()








