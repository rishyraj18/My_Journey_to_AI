from core.userfunctionalities.order import order
from core.adminfunctionalities.product import products


class cart:
    cart = {}
    def __init__(self, cart_ID):
        self._cart_ID = cart_ID
        self._product_list = {}

    def add_products(self, product):
        if product in products.inventory:
            if product not in self._product_list:           
                self._product_list[product] = {
                    'name' : products.inventory[product]._product_name,
                    'price' : products.inventory[product]._product_price,
                    'quantity' : 1
                }
                temp = products.inventory[product]._product_name
                print(f"Product Added : {temp}")
            else:
                self._product_list[product]["quantity"] += 1
                self._product_list[product]['price'] += products.inventory[product]._product_price
                temp = products.inventory[product]._product_name
                print(f"Product Added : {temp}")
        else:
            print("Unbale to find the Product ID")

    def remove_product(self):
        product = input("Please Enter Product ID: ")
        if product in products.inventory:
            if product not in self._product_list:
                print("Product Not Added in Cart")        
                self._product_list[product] = {
                    'name' : products.inventory[product]._product_name,
                    'price' : products.inventory[product]._product_price,
                    'quantity' : 1
                }
                temp = products.inventory[product]._product_name
                print(f"Product Removed : {temp}")
            elif self._product_list[product]["quantity"] == 1:
                del self._product_list[product]
            else:
                self._product_list[product]["quantity"] -= 1
                self._product_list[product]['price'] -= products.inventory[product]._product_price
                temp = products.inventory[product]._product_name
                print(f"Product Removed: {temp}")
        else:
            print("Unbale to find the Product ID")


    def display_cart(self):
        if self._product_list == {}:
            print("cart is Empty")

        for pid, details in self._product_list.items():
            print(f"""
Product Name: {[details["name"]]} 
Price : {[details["price"]]}
Quantity : {[details["quantity"]]}""")

    def calculate_total(self):
        sub_total = 0
        for product in self._product_list:
            sub_total += self._product_list[product]["price"]

        print(f"The Sub-total for products in cart (₹): {sub_total}")

    def total_quantity(self):
        quantity = 0
        for product in self._product_list:
            quantity += self._product_list[product]["quantity"]

    def placeorder(self):
        sub_total = 0
        for product in self._product_list:
            sub_total += self._product_list[product]["price"]
        quantity = 0
        for product in self._product_list:
            quantity += self._product_list[product]["quantity"]
        items = []
        for product in self._product_list:
            items.append(self._product_list[product]["name"])
        self._cart_ID = order(self._cart_ID, sub_total, quantity, items)

def create_cart(uname):
    cart.cart[uname] = cart(uname)