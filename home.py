from typing import Any


class store:
    def __init__(self):
        self.name = ""
        self.location = ""

    def set_info(self):
        #this loop will keep repeating until the string is not empty
        while True:
            name = input("Good morning!! which store would you want to use today?\n>>> ")    
            if not name.strip():
                print("Invalid enter a name")
            else:
                self.name = name
                break
        while True:
            location = input("Which location you want to use?\n>>> ")
            if not location.strip():
                print("Invalid enter a location")
            else:
                self.location = location
                break
    def __str__(self):
        print("Store:", self.name)
        print ("Location:", self.location)
    

class cart:
    def __init__(self):
        self.product_name = ""
        self.cart = {}
        self.quantity = 0
        self.receipt = ""
        
    # removes item from dictionary
    def remove_item(self):
        for i in self.cart:
            list += 1
            print(str(list) + ":", i)
        print("enter the name of the item you want to remove\n>>> ")
    #Adds item to dictionary
    def add_item(self, product_name, quantity):
        self.cart[product_name] = quantity
        print(f"You added {quantity} of {product_name}")
def menu():
    print("Products as follow")
    print("Milk: $2.50\nBread: $1.98\nEgg: $0.70\nFlour: $1.18\nOil: $4.00\nCheese: $2.68\n")
while True:
    s = store()
    s.set_info()
    menu()
