from typing import Any


class store:
    def __init__(self):
        self.name = ""
        self.location = ""

    def set_var(self, name, location):
        if not name.strip():
            print("Invalid enter a name")
        else:
            self.name = name
        if not location.strip():
            print("Invalid enter a location")
        else:
            self.location = location
    def __str__(self):
        print("Store:", self.name)
        print ("Location:", self.location)


class cart:
    def __init__(self, product_name, quantity, receipt):
        self.product_name = product_name
        self.quantity = quantity
        self.receipt = receipt
        self.cart = {}
