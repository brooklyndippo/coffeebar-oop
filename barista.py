from person import Person

class Barista(Person):
    def __init__(self, name, favorite_drink, wallet, tip_percent, greeting):
        super().__init__(name, favorite_drink, wallet, tip_percent)
        self.greeting = greeting
        self.tips = 0
    
    def greet_customer(self):
        print(self.greeting)
        return

    def tip_jar(self, order):
        self.tips += order.tip
