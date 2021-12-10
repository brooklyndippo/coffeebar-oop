class Order(object):
    def __init__(self, type, person, price=0, tip=0, total=0):
        self.type = type
        self.person = person
        self.price = price
        self.tip = tip
        self.total = total

    def to_string(self):
        order_up = f'{self.person.name} orders: {self.type}'
        print(order_up)
        return 