class Item:

    # we can restrict the expected type using a common sign followed by the data type
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
            # let's add an assert statement
                # check if there is a match between what's haping and the expectations
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 3000, 3)
