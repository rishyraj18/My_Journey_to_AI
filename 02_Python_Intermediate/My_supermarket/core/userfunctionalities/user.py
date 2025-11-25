class user:
    userdetails = {}

    def __init__(self, username, password, Name, phonenumber, location, orders = 0):
        self.__username = username
        self._password = password
        self.__name = Name
        self.__phonenumber = phonenumber
        self.__location = location
        self.__orders = orders
    
    def display_userdetails(self):
        print(f"login Username : {self.__username}\n"
              f"Name : {self.__name}\n"
              f"Phone number : {self.__phonenumber}\n"
              f"Location of the user : {self.__location}")
    
def  new_user():
    uname = input("Please enter username: ")
    passwd = input("Please enter Password: ")
    Name = input("Please Enter display Name: ")
    phonenumber = input("Please enter your Phone Number: ")
    location = input("Please Enter your location :")
    user.userdetails[uname] = user(uname, passwd, Name, phonenumber, location)

