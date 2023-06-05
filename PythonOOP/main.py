# What if we want to restrict the user to modify critical attributes like "name"


from item import Item

item1 = Item("MyItem", 750)

# scenario: try to modify defined attribute
# item1.name = "OtherItem"

# scenario: try to access a private attribute
# print(item1.__name)

# scenario: try to modify defined attribute after the name.setter decorator
item1.name = "OtherItem"
print(item1.name)