from order.menu.MenuItem import MenuItem


class ItemComposite(MenuItem):
    def __init__(self, title):
        self.title = title
        self.items = []

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.get_price()
        return price

    def get_name(self):
        items = "*** " + self.title + " ***"
        for item in self.items:
            items += " - " + item.get_name()
        return items

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)
