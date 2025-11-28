from core.adminfunctionalities.product import add_products, product_quantity, product_price, products
from core.userfunctionalities.cart import cart
from core.userfunctionalities.user import user
from core.userfunctionalities.order import order
from utilitis.validations import product_validation
from utilitis.exceptions import product_validation_error


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
                  "8. User Profile Managment\n"
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
                        try:
                              product_validation(product_ID)
                              print("validated")
                              cart.cart_List[username].add_products(product_ID)
                        except product_validation_error as message:
                              print(message)
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
                        print("------------User Profile Management------------------")
                        print("1. Change Password\n"
                              "2. Change Phone Number\n"
                              "3. Change Location\n")
                        inp =(input("Please Select your option: "))
                        if inp == '1':
                              print("Password Reset")
                              new_password = input("Please enter your new password : ")
                              user.userdetails[username].change_password(new_password)
                        elif inp == '2':
                              print("Phone number---- Update")
                              new_phnumber = input("Please enter your new Phone Number : ")
                              user.userdetails[username].change_phonenumber(new_phnumber)
                        elif inp == '3':
                              print("Location----Update")
                              new_location = input("Please enter your new Location : ")
                              user.userdetails[username].change_location(new_location)
                        else:
                              print("Please Select correct option")

                  case 9:
                        print("------------Admin Controls---------")
                        print("1. Add Product\n"
                              "2. Change Product Price\n"
                              "3. Update Quantity\n")
                        inp =(input("Please Select your option: "))
                        if inp == '1':
                              add_products()
                        elif inp == '2':
                              product_price()
                        elif inp == '3':
                              product_quantity()
                        else:
                              print("Please Select correct option")

                  case _:
                        print("Please enter correct option")
                        
      print("Exiting RR Commerce Application")
      exit()