class Item:
    # functions inside classes are called methods
    def calculate_total_price(self, x, y):
        # self is the commmon convention for dev
        # the item will be passed automatically to the method
        return x * y



# here we have a relationship the four lines of code below
# assigned to one instance of the class, in this case item1 = Item()
item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))


# the problem in this example is the fact we don't have a set of rules
# for the attributes we would like to pass in to instantiate the instance

# for each item that we want to create we need to hardcode the attribute name