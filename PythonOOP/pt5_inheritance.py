# let's say we have broken phones that we can't sell
# at first instance the logic step is to create a method to substract the broken phones
# the problem is that we can't go inside the item class. because this method is not going to be useful for other items
# the best practice is to create a separate class that inherits the functionalities that the item class brings with it

import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # this is a class method
    @classmethod # -> quick way to change the behaviour of the function, decorator
    def instantiate_from_csv(cls): # the class object itself is passed as the first argument
        with open("PythonOOP/items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod # static methods never send to the background the instance as the first argument
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e.: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self): # representing your objects, watch video comparing with __str__ magic method
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"


# this is a child class from the Item class
# the code below is not a best practice, because we'll have duplicated code
# we need to use the magic method super() function to inherit the parent instances

# class Phone(Item):
#     all = []
#     def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
#         assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero!"

#         # assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.broken_phones = broken_phones

#         # Actions to execute
#         Phone.all.append(self)


class Phone(Item):
    # name, price, and quantity are repeated code, we can avoid this with kwargs --> research later
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero!"

        # assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all)
print(Phone.all)