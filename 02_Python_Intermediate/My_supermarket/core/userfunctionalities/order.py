from core.adminfunctionalities.product import products


class order:
    list_of_orders = {}

    def __init__(self, Order_ID, Total_amount, no_of_items, items):
        self._Order_ID = Order_ID
        self._Total_amount = Total_amount
        self._no_of_items = no_of_items
        self._items = items

    def display_order_details(order_ID):
        for order_id in order.list_of_orders:
            print(f"""
Order ID : {order.list_of_orders[order_ID]._Order_ID}
Total Amount : {order.list_of_orders[order_ID]._Total_amount}
Items : {order.list_of_orders[order_ID]._items}
Total No of Items : {order.list_of_orders[order_ID]._no_of_items}
    """)

def create_order(Order_ID,Total_amount, no_of_items, Items):
    order.list_of_orders[Order_ID] = order(Order_ID, Total_amount, no_of_items,Items)
    print("Order Placed, Successfully......")
    order.display_info(Order_ID)
