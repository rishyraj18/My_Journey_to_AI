from abc import ABC , abstractmethod

class weapon(ABC):
    def __init__(self, name, damage, Energy_Cost):
        self._name = name
        self._damage = damage
        self._Energy_Cost = Energy_Cost

    @abstractmethod
    def fire(self):
        return (self._damage, self._Energy_Cost)

class Laser_Weapon(weapon):
    def __init__(self, name, damage = 100, Energy_Cost = 25):
        super().__init__(name, damage, Energy_Cost)

    def fire(self):
        return super().fire()
    
    def see_my_weapon(self):
            print(f"{self.__class__.__name__}")
class Plasma_Weapon(weapon):
    def __init__(self, name, damage = 120, Energy_Cost = 40):
        super().__init__(name, damage, Energy_Cost)

    def fire(self):
        return super().fire()

    def see_my_weapon(self):
        print(f"{self.__class__.__name__}")