class user:
    userdetails = {}

    def __init__(self, username, password, Name, phonenumber, location, orders = 0):
        self._username = username
        self._password = password
        self._name = Name
        self._phonenumber = phonenumber
        self._location = location
        self._orders = orders
    
    def display_userdetails(self):
        print(f"login Username : {self.__username}\n"
              f"Name : {self.__name}\n"
              f"Phone number : {self.__phonenumber}\n"
              f"Location of the user : {self.__location}")
    
    def change_password(self, new_password):
        self._password = new_password
        print("Password changed successfully")

    def change_phonenumber(self, new_phone):
        self._phonenumber = new_phone
        print("Phonenumber changed successfully")

    def change_location(self, new_location):
        self._location = new_location
        print("Location changed successfully")

def  new_user():
    uname = input("Please enter username: ")
    passwd = input("Please enter Password: ")
    Name = input("Please Enter display Name: ")
    phonenumber = input("Please enter your Phone Number: ")
    location = input("Please Enter your location :")
    user.userdetails[uname] = user(uname, passwd, Name, phonenumber, location)

user.userdetails["RishyRaj"] = user("RishyRaj", "RR", "Rishy Raj S M", "9080976475", "Erode")

#Ri$hyr@j18122003