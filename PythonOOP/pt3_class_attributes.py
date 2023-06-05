class Item:
    # create class attribute
    pay_rate = 0.8 # The pay rate after 20% discount

    # below is a special method, a constructor that has special features (magic method)
    def __init__(self, name, price, quantity=0):

        self.name = name
        self.price = price
        self.quantity = quantity

    # recall the object itself is passed as an argument
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # --> self can overwrite an attribute belonging to an instance level


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 2)
item2.pay_rate = 0.7 # --> here we assign a different pay rate for the item no. 2, this class attribute is assigned to the instance
item2.apply_discount()
print(item2.price)

# print(Item.__dict__) # Magic attribute --> gives all attributes for class level
# print(item1.__dict__) # Magic attribute --> gives all attributes for instance level
