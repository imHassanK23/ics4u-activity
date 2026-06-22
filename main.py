# ICS4U Activity

class store_item:
    def __init__(self, n, p):
        self.itemName = n # name
        self.cost = p # price

    def getname(self): return self.itemName

    def setname(self, n): self.itemName = n

    def getprice(self): return self.cost

    def setprice(self, p): self.cost = p

    # getname() gives back the item name
    # setprice(50) changes price to 50

    def show_info(self):
        print(self.itemName + " is worth $" + str(self.cost))
    # prints the cost of a store item

class plug_in_item(store_item):
    def __init__(self, n, p, w): # takes extra aurguement w which is warrenty
        super().__init__(n, p)
        self.warranty = w

    def show_info(self):
        print(self.getname() + " is worth $" + str(self.getprice()) + " with " + str(self.warranty) + " yr warranty")
    # printes cost and warrenty of  plug in item

my_inventory = [
    store_item("apple", 2),
    plug_in_item("tv", 500, 2),
    plug_in_item("laptop", 1000, 1)
]

print("Items: TV, Apple, Laptop")
user_search = input("enter item to search: ")

# loop to find the item
found_it = False
for i in my_inventory:
    if i.getname() == user_search: # Checks if this object's name matches what the user typed
        i.show_info()
        found_it = True

        try:
            new_val = int(input("enter new price for " + i.getname() + ": "))
            i.setprice(new_val) # update item price
            print("updated:")
            i.show_info()
        except ValueError:
            print("crashed because u didnt type a number")

if not found_it:
    print("item not found")
