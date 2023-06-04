class Item:
    # below is a special method, a constructor that has special features (magic method)
    def __init__(self, name, price, quantity=0):
        # we can assign the attributes in this self method --> dynamic attribute assignment
        # you can assign attributes to specific instances individually
            # for instance you want to check if the laptop has numpad, this is unrealistic of a phone
            # so, we can assign an specific attribute to an instance
        self.name = name
        self.price = price
        self.quantity = quantity

        # reacall the object itself is passed as an argument
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())