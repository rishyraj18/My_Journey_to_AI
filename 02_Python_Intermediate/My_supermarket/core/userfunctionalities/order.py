from core.adminfunctionalities.product import products


class order:
    list_of_orders = {}

    def __init__(self, Order_ID, Total_amount, no_of_items, items):
        self._Order_ID = Order_ID
        self._Total_amount = Total_amount
        self._no_of_items = no_of_items
        self._items = items
        print("Order Placed, Successfully")

    def display_order_details(order_id):
        for order_id, details in order.list_of_orders.items():
            print(f"""Order ID : {[details["Order ID"]]}
Items = {[details["Items"]]}
Total Amount : {[details["Total Amount"]]}""")