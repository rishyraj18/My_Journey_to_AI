class Robots:
    def __init__(self, name, speed, energy):
        self.__name = name
        self.__speed = speed
        self.__energy = energy

    def move(self, rate, energy):
        self.__energy = max(0, self.__energy - energy)
        print(f"Moving at {(self.__speed * rate):.0f}; Energy Left :{self.__energy:.0f}")


    def recharge(self, amount):
        self.__energy = min(100, self.__energy + amount)
        print(f"You Robot {self.__name} is recharged to {self.__energy:.0f}")

    def status(self):
        print(f"Your Robot {self.__name}'s Info\nMovment Speed: {self.__speed}\nEnergy left: {self.__energy:.0f}\n")

class WheeledRobot(Robots):
    energy_consumption = 10
    def __init__(self, name, speed, energy):
        super().__init__(name, speed, energy)
    
    def move(self):
        if self._Robots__energy >= 10:
            if self._Robots__energy > 70:
                rate = 1.5
                super().move(rate,WheeledRobot.energy_consumption)
            elif self._Robots__energy > 50:
                rate  = 1.2
                super().move(rate,WheeledRobot.energy_consumption)
            else:
                rate = 1
                super().move(rate,WheeledRobot.energy_consumption)
        else:
            print("Your Robot is Out of Energy")

class HumanoidRobot(Robots):
    energy_consumption = 15
    def __init__(self, name, speed, energy):
        super().__init__(name, speed, energy)
    
    def move(self):
        if self._Robots__energy >= 15:
            super().move(1,HumanoidRobot.energy_consumption)
        elif self._Robots__energy < 15:
            print("Your Robot Does not have energy")
        else:
            print("Your Robot is Out of Energy")

class FlyingRobot(Robots):
    energy_consumption = 25
    def __init__(self, name, speed, energy):
        super().__init__(name, speed, energy)
    
    def move(self):
        if self._Robots__energy >= 25:
            if self._Robots__energy > 60:
                rate = 2
                super().move(rate,FlyingRobot.energy_consumption)
            elif self._Robots__energy > 50:
                rate  = 1.2
                super().move(rate,FlyingRobot.energy_consumption)
            else:
                rate = 1
                super().move(rate,FlyingRobot.energy_consumption)
        else:
            print("Your Robot is Out of Energy")


R1 = WheeledRobot("r1", 100, 80)
R2 = HumanoidRobot("r2", 80, 95)
R3 = FlyingRobot("r3", 150, 85)

operation = None

while operation != "EXIT":
    operation = str(input("What you want to do (move / recharge / get_info / Exit): ")).strip().upper()
    if operation == "MOVE":
        move_operation = str(input("Please select the Robot (R1/R2/R3): ")).upper()
        if move_operation == "R1":
            R1.move()
        elif move_operation == "R2":
            R2.move()
        elif move_operation == "R3":
            R3.move()
        else:
            print("Entered wrong Robot Name, try again")
    elif operation == "RECHARGE":
        recharge_operation = str(input("Please select the Robot (R1/R2/R3): ")).upper()
        energy = int(input ("Enter recharge Amount max 100: "))
        if 0 < energy < 100:
            if recharge_operation == "R1":
                R1.recharge(energy)
            elif recharge_operation == "R2":
                R2.recharge(energy)
            elif recharge_operation == "R3":
                R3.recharge(energy)
            else:
                print("Entered wrong Robot Name, try again")
        else:
            print("Entered wrong enegry value")

    elif operation == "GET_INFO":
        info_operation = str(input("Please select the Robot (R1/R2/R3): ")).upper()
        if info_operation == "R1":
            R1.status()
        elif info_operation == "R2":
            R2.status()
        elif info_operation == "R3":
            R3.status()
        else:
            print("Entered wrong Robot Name, try again")
    elif operation == "EXIT":
        print("Exiting the Game")
        break
    else:
        print("Enter Wrong Operation")