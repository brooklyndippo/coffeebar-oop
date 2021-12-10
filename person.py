from order import Order

class Person(object):
    def __init__(self, name, favorite_drink, wallet, tip_percent):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_percent = tip_percent

    def my_order(self):
        order = Order(self.favorite_drink, self)
        return order

    def pay_for_order(self, order):
        self.wallet -= order.total
        print(f' | {self.name} paid ${order.price} for their {self.favorite_drink} and tipped ${order.tip}.')
        print(f' | {self.name} has ${self.wallet} remaining in their wallet.')