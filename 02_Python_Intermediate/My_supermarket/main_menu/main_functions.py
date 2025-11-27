from core.adminfunctionalities.product import products, add_products, product_quantity, product_price
from utilitis.validations import product_validation
from core.userfunctionalities.cart import cart
from core.userfunctionalities.user import user, new_user
from core.userfunctionalities.order import order

def main_menu(username):
      username = username
      inp = None
      while inp != 0:
            print("Main Menu :-")
            print("1. Get Product List\n"
                  "2. Add products to Cart\n"
                  "3. List products in cart\n"
                  "4. Remove Product from Cart\n"
                  "5. Sub-total for Cart\n"
                  "6. Place order\n"
                  "7. Get my order Details\n"
                  "8. User Registration\n"
                  "9. Admin Controls\n"
                  "0. Exit")

            try:
                  inp = int(input("Please enter your option: "))
            except ValueError:
                  print("Please enter correct option")

            match inp:
                  case 1:
                        products.print_all_products()
                  case 2:
                        product_ID = input("Please enter the product ID: ")
                        if product_validation(product_ID):
                              cart.cart[username].add_products(product_ID)
                  case 3:
                        cart.cart_List[username].display_cart()
                  case 4:
                        cart.cart_List[username].remove_product()
                  case 5:
                        cart.cart_List[username].calculate_total()
                  case 6:
                        cart.cart_List[username].placeorder()
                  case 7:
                        order.display_order_details(username)
                  case 8:
                        print("Please Enter the Below Details to create new user")
                        new_user()
                  case 9:
                        print("------------Admin Controls---------")
                        print("1. Add Product\n"
                              "2. Change Product Price\n"
                              "3. Update Quantity\n")
                        inp =int(input("Please Select your option: "))
                        if inp == 1:
                              add_products()
                        elif inp == 2:
                              product_price()
                        elif inp == 3:
                              product_quantity()
                        else:
                              print("Please Select correct option")

                        
      print("Exiting RR Commerce Application")
      exit()