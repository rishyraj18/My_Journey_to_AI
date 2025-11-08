class Vehicle:
    total_no_of_vehicle = 0
    no_of_vehicle_in_garage = 0

    def __init__(self, vehicle_no, rent_rate, status = "Registered and Available to rent"):
        self.__Vehicle_no = vehicle_no
        self.__rent_rate = rent_rate
        self.__status = status
        print(f"Vehicle registred:-\nVechicle No : {self.__Vehicle_no}\nrent per hour: {self.__rent_rate}")
        Vehicle.total_no_of_vehicle += 1
        Vehicle.no_of_vehicle_in_garage +=1

    def rent_calculation(self,no_of_hours):
        print(f"Rent to be paid for the Vehicle with 18% Tax : ${((self.__rent_rate)*no_of_hours)*1.18}")

    def rent_vehicle(self):
        self.__status = "Vehicle Rented"
        print(f"Vehicle Rented; Rent per hour is {self.__rent_rate}")
        Vehicle.no_of_vehicle_in_garage -= 1
        
    def vehicle_return(self):
        self.__status = "In the Garage"
        print("Car returned and Parked in garage")

    def change_rent(self, chg_rent):
        self.__rent_rate = chg_rent
        print(f"Rent of the car is changed to {self.__rent_rate}")
    
    @classmethod
    def vehicle_available(cls):
        print(f"Total no of cars Available in the Garage: {cls.no_of_vehicle_in_garage}")

    @classmethod
    def total_vehicle(cls):
        print(f"Total no of cars registred: {cls.total_no_of_vehicle}")

class car(Vehicle):

    def __init__(self, vehicle_no, rent_rate, status="Registered and Available to rent"):
        super().__init__(vehicle_no, rent_rate, status)
        print("Vehicle Type: Car")

    def type(self):
        print("Type of Vehicle: Car")

class bike(Vehicle):

    def __init__(self, vehicle_no, rent_rate, status="Registered and Available to rent"):
        super().__init__(vehicle_no, rent_rate, status)
        print("Vehicle Type: Bike")

    def type(self):
        print("Type of Vehicle: Bike")

class truck(Vehicle):

    def __init__(self, vehicle_no, rent_rate, status="Registered and Available to rent"):
        super().__init__(vehicle_no, rent_rate, status)
        print("Vehicle Type: Truck")

    def type(self):
        print("Type of Vehicle: Truck")



c1 = car(54321, 11)
b1 = bike(12345, 7)
t1 = truck(98765, 16)

c1.rent_vehicle()

Vehicle.vehicle_available()
Vehicle.total_vehicle()