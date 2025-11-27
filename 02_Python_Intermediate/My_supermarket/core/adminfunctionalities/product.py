class products:
    inventory = {}
    
    def __init__(self, product_ID, product_name, product_price, product_quantity):
        self._product_ID = product_ID
        self._product_name = product_name
        self._product_price = int(product_price)
        self._product_quantity = product_quantity
    
    def print_all_products():
        print("\n--------------------Products List---------------------------")
        i = 1
        for pid in products.inventory:
            print("Product = {i}")
            i += 1
            print(f"Product ID : {products.inventory[pid]._product_ID}")
            print(f"Product Name : {products.inventory[pid]._product_name}")
            print(f"Product Price : {products.inventory[pid]._product_price}")
            print(f"Product Quantity : {products.inventory[pid]._product_quantity}")
        
    def change_product_price(self, n_price):
        if self._product_ID in products.inventory:
            products.inventory[self._product_ID]["price"] = n_price
        else:
            print("Product details unavailable")

    def update_quantity(self,n_quantity):
        if self._product_ID in products.inventory:
            products.inventory[self._product_ID]["quantity"] = n_quantity
        else:
            print("Product details unavailable")

products.inventory["P1"] = products("P1", "Laptop", 50000, 5)
products.inventory["P1"] = products("P1", "Mobile", 20000, 5)

def add_products():
    pid = input("Please enter product ID: ")
    product_name = input("Please enter product name: ")
    product_price = input("Please enter product price: ")
    product_quantity = input("Please enter product quantity: ")
    products.inventory[pid] = products(pid,product_name, product_price, product_quantity)


def product_price():
    pid = input("Please enter product ID: ")
    product_price = input("Please enter product price: ")
    products.inventory[pid].change_product_price(product_price)

def product_quantity():
    pid = input("Please enter product ID: ")
    product_quantity = input("Please enter product quantity: ")
    products.inventory[pid].update_quantity(product_quantity)

