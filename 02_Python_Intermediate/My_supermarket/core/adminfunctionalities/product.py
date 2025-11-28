class products:
    inventory = {}
    
    def __init__(self, product_ID, product_name, product_price, product_quantity):
        self._product_ID = product_ID
        self._product_name = product_name
        self._product_price = int(product_price)
        self._product_quantity = int(product_quantity)
            
    def print_all_products():
        print("\n--------------------Products List---------------------------")
        i = 1
        for pid in products.inventory:
            print(f"Product = {i}")
            i += 1
            print(f"Product ID : {products.inventory[pid]._product_ID}")
            print(f"Product Name : {products.inventory[pid]._product_name}")
            print(f"Product Price : {products.inventory[pid]._product_price}")
            print(f"Product Quantity : {products.inventory[pid]._product_quantity}")
            print("-------------------------------------------------------------------\n")
        
    def change_product_price(self, n_price):
        if self._product_ID in products.inventory:
            self._product_price = n_price
        else:
            print("Product details unavailable")

    def update_quantity(self,n_quantity):
        if self._product_ID in products.inventory:
            self._product_quantity = n_quantity
        else:
            print("Product details unavailable")

products.inventory["P1"] = products("P1", "Laptop", 45000, 20)
products.inventory["P2"] = products("P2", "Mobile",  20000, 15)
products.inventory["P3"] = products("P3", "IPAD", 35000, 10)
products.inventory["P4"] = products("P4", "MacBook", 60000, 30)
products.inventory["P5"] = products("P5", "IMAC Desktop PC", 100000, 20)

def add_products():
    pid = input("Please enter product ID: ")
    product_name = input("Please enter product name: ")
    product_price = input("Please enter product price: ")
    product_quantity = input("Please enter product quantity: ")
    products.inventory[pid] = products(pid,product_name, product_price, product_quantity)
    print(f"Product : {product_name}, Added")

def product_price():
    pid = input("Please enter product ID: ")
    product_price = input("Please enter product price: ")
    products.inventory[pid].change_product_price(product_price)
    print("Product Price, updated")

def product_quantity():
    pid = input("Please enter product ID: ")
    product_quantity = input("Please enter product quantity: ")
    products.inventory[pid].update_quantity(product_quantity)
    print("Product Quantity, Updated")
