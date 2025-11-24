class products:
    inventory = {}
    
    def __init__(self, product_ID, product_name, product_price, product_quantity):
        self._product_ID = product_ID
        self._product_name = product_name
        self._product_price = product_price
        self._product_quantity = product_quantity

        products.inventory[self._product_ID] = {
            "name": product_name,
            "price": product_price,
            "quantity": product_quantity
        }

    @staticmethod
    def print_all_products():
        print("\n===== PRODUCT INVENTORY =====")
        if not products.inventory:
            print("No products available.")
            return
        
        for pid, details in products.inventory.items():
            print(f"""
Product ID   : {pid}
Name         : {details['name']}
Price        : {details['price']}
Quantity     : {details['quantity']}
            """)

        
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

p1 = products("p1", "Laptop", 50000, 200)
p2 = products("p2", "Mobile phones", 20000, 500)

products.print_all_products()