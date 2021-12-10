from person import Person
from barista import Barista

class CoffeeBar(object):
    def __init__(self, name, barista, orders=[]):
        self.name = name
        self.barista = barista
        self.orders = orders
        self.receipts = []
        self.register = 50.00
        self.daily_profit = 0.00

    def place_order(self, order):
        if order.type == 'Coffee':
            order.price = 2.05
        elif order.type == 'Tea':
            order.price = 1.55
        elif order.type == 'Milk':
            order.price = 2.95

        #calculate and add the tip
        order.tip = round(order.price * order.person.tip_percent, 2)
        order.total = order.price + order.tip            
        self.orders.append(order)
        return self.orders

    def process_orders(self):
        print('---processing orders---\n')
        self.barista.greet_customer()
        print('\n')
        for order in self.orders:
            order.to_string() #print the order
            order.person.pay_for_order(order) #subtract payment from wallet
            self.add_register(order) #add to coffee bar register
            self.barista.tip_jar(order) #tip the barista
            self.receipts.append(order) #move to receipts
            print('\n')
        self.orders = []
        return

    def add_register(self, order):
        self.register += order.price
        self.daily_profit += order.price
        return

    def cash_out(self):
        print(f'\nAnother great day at {self.name}! \n  * {self.barista.name} brewed up a lot of coffee and made ${self.barista.tips} in tips.\n  * The shop made ${self.daily_profit} today and cashed out with ${self.register} in the register.\n')


# ENTER python3 coffee_bar.py IN THE TERMINAL TO RUN THE COFFEE BAR 

amy = Person('Amy', 'Coffee', 20.00, .20)
bob = Person('Bob', 'Tea', 5.25, .18)
cat= Person('Cat', 'Milk', 91.00, .15)

kevin = Barista('Kevin', 'cappuccino', 5.00, 0, 'Hey dude!')

common_grounds = CoffeeBar('Common Grounds', kevin)
print(f'\n☕ Welcome to {common_grounds.name} ☕\n')

common_grounds.place_order(amy.my_order())
common_grounds.place_order(bob.my_order())
common_grounds.place_order(cat.my_order())
common_grounds.process_orders()

common_grounds.cash_out()