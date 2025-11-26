
class Inputvalidation(Exception):
    def main_menu(inp):
        if inp  > 9:
            print("Please Enter Correct option")
        elif inp.isalpha() or inp.alnum() or inp.isspace():
            print("Please enter the number for the option")
        else:
            print("Error Occured, please try again")

class login_password_invalid(Exception):
    def __init__(self, message = "Invalid Password"):
        self.message = message
        super().__init__(self.message)

class login_username_invalid(Exception):
    def __init__(self, message = "Invalid UserName\nPlease try-again"):
        self.message = message
        super().__init__(self.message)

class product_validation(Exception):
    def __init__(self, message = "Unbale to find the Product ID"):
        self.messaga = message
        super().__init__(self.messaga)