from core.userfunctionalities.order import order, create_order
from core.adminfunctionalities.product import products
from utilitis.validations import product_validation_error

class cart:
    cart_List= {}
    def __init__(self, cart_ID):
        self._cart_ID = cart_ID
        self._product_list = {}


    def add_products(self, PID):
        if PID not in self._product_list:
            self._product_list[PID] = {
                'name' : products.inventory[PID]._product_name,
                'price' : products.inventory[PID]._product_price,
                'quantity' : 1
            }
            temp = products.inventory[PID]._product_name
            print(f"Product Added : {temp}")
        else:
            self._product_list[PID]["quantity"] += 1
            self._product_list[PID]["price"] += products.inventory[PID]._product_price
            temp = products.inventory[PID]._product_name
            print(f"Product Added : {temp}")

    def remove_product(self):
        PID = input("Please Enter Product ID: ")
        if PID in self._product_list:
            if PID not in self._product_list:
                print("Product Not Added in Cart")
            elif self._product_list[PID]["quantity"] == 1:
                del self._product_list[PID]           
            else:
                self._product_list[PID]["quantity"] -= 1
                self._product_list[PID]['price'] -= products.inventory[PID]._product_price
                temp = products.inventory[PID]._product_name
                print(f"Product Removed: {temp}")

    def display_cart(self):
        if self._product_list == {}:
            print("cart is Empty")

        for product in self._product_list:
            print(f"""
Product Name: {self._product_list[product]["name"]} 
Price : {self._product_list[product]["price"]}
Quantity : {self._product_list[product]["quantity"]}""")

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
        Order_ID = self._cart_ID
        Total_amount = 0
        no_of_items = 0
        Items = []
        for product in self._product_list:
            products.inventory[product]._product_quantity -= self._product_list[product]["quantity"]
            Total_amount += self._product_list[product]["price"]
            no_of_items += self._product_list[product]["quantity"]
            Items.append(self._product_list[product]["name"])
        create_order(Order_ID,Total_amount, no_of_items, Items)
        self._product_list = {}
          

def create_cart(uname):
    cart.cart_List[uname] = cart(uname)