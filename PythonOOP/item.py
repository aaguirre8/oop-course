import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        print("You're trying to get name")
        return self.__name      # the attribute is hidden
    
    @name.setter
    # this allows to skip the property decorator and allow the user to set the name property
    def name(self, value):
        print("You're trying to set")
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

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