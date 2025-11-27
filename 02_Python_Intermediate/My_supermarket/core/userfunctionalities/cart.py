from core.userfunctionalities.order import order,create_order
from core.adminfunctionalities.product import products
from utilitis.validations import product_validation
























































































































'''
class cart:
    cart_List= {}
    def __init__(self, cart_ID):
        self._cart_ID = cart_ID + "cart"

    def add_products(self, product):
        if product_validation(product):
            if self._cart_ID not in cart.cart_List: 
                cart.cart_Lis[self._cart_ID] = {
                    'Pid' : products.inventory[product]._product_ID,
                    'name' : products.inventory[product]._product_name,
                    'price' : products.inventory[product]._product_price,
                    'quantity' : 1
                }
                temp = cart.cart_List[self._cart_ID]["name"]
                print(f"Product Added : {temp}")
            else:
                cart.cart_List[self._cart_ID]["quantity"] += 1
                cart.cart_List[self._cart_ID]["price"] += products.inventory[product]._product_price
                temp = cart.cart_List[self._cart_ID]["name"]
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

    def display_cart(self):
        if self._product_list == {}:
            print("cart is Empty")

        for cart_ID in cart.cart_List:
            print(f"""
Product Name: {cart.cart_List[cart_ID]["name"]} 
Price : {cart.cart_List[cart_ID]["price"]}
Quantity : {cart.cart_List[cart_ID]["quantity"]}""")

    def calculate_total(self):
        sub_total = 0
        for cart_ID in cart.cart_List:
            quantity += cart.cart_List[cart_ID]["price"]

        print(f"The Sub-total for products in cart (₹): {sub_total}")

    def total_quantity(self):
        quantity = 0
        for cart_ID in cart.cart_List:
            quantity += cart.cart_List[cart_ID]["quantity"]

    def placeorder(self):
        Order_ID = self._cart_ID
        Total_amount = 0
        no_of_items = 0
        Items = []
        for cart_ID in cart.cart_List:
            Total_amount += cart.cart_List[cart_ID]["price"]
            no_of_items += cart.cart_List[cart_ID]["quantity"]
            Items.append(cart.cart_List[cart_ID]["Name"])
        order.create_order(Order_ID,Total_amount, no_of_items, Items)
          

def create_cart(uname ):
    cart.cart_List[uname+ "cart"] = cart(uname +"cart")
'''
