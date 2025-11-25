from core.userfunctionalities.user import user, new_user
from utilitis.validations import verify_Login
from utilitis.exceptions import Inputvalidation, login_password_invalid, login_username_invalid, product_validation
from core.userfunctionalities.cart import cart, create_cart
from core.adminfunctionalities.product import products
from main_menu.main_functions import main_menu


print("Welcome to RR Ecommerce")

def login_fuction():
            try:
                  username = input("Please enter your username: ")
                  password = input("Please enter you password: ")
                  verify_Login(username, password)
                  print("Login Successfull")
                  create_cart(username)
                  main_menu(username)
            except (login_password_invalid, login_username_invalid) as message:
                  print(message)

def initializing_module():
      print("1: Login to Initialization\n"
      "2. Create New User\n")

      initial_input = int(input("Please select you option: "))
      while initial_input !=1 or initial_input !=2:
            if initial_input == 1:
                  #initialing User Login
                  login_fuction()
            elif initial_input == 2:
                  new_user()
                  initializing_module()
            else:
                  print("Wrong option seleteced")
                  initializing_module()

initializing_module()
