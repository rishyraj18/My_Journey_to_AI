class user:
    userdetails = {}

    def __init__(self, username, password, Name, phonenumber, location, orders = 0):
        self.__username = username
        self.__password = password
        self.__name = Name
        self.__phonenumber = phonenumber
        self.__location = location
        self.__orders = orders

    def change_password (self, n_password):
        self.__password = n_password
        print(f"Password reset for the user: {self.__name}")

    def change_phonenumber(self,n_phonenumber):
        self.__phonenumber = n_phonenumber
        print(f"Phone number changed for thr user : {self._name}")
        print(f"New Phone number: {self.__phonenumber}")

    def change_location(self, location):
       self.__location = location
       print(f"Location changed for the user : {self.__name}")
       print(f"New Location : {self.__location}") 
    
    def display_userdetails(self):
        print(f"login Username : {self.__username}\n"
              f"Name : {self.__name}\n"
              f"Phone number : {self.__phonenumber}\n"
              f"Location of the user : {self.__location}")