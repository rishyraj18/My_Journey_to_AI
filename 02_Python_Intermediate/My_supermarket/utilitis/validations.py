from utilitis.exceptions import login_password_invalid, login_username_invalid, product_validation_error
from core.userfunctionalities.user import user
from core.adminfunctionalities.product import products
from core.userfunctionalities.cart import cart

def verify_Login(username, password):
    if username in user.userdetails:
        if password != user.userdetails[username]._password:
            raise login_password_invalid
    elif username not in user.userdetails:
        raise login_username_invalid

def product_validation(product_id):
    if product_id in products.inventory:
        return True
    else:
         raise product_validation_error
    