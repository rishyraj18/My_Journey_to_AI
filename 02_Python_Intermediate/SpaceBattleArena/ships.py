from abc import ABC, abstractmethod
from utility import log_decorator

class Baseship(ABC):
    def __init__(self, Player_name,health, shield, power):
        self._player_name = Player_name
        self._health = health
        self._shield = shield
        self._power = power
        
    def take_damage(self,other):
        if other._shield > 100:
            other._health = int(other._health - self._power/2)
            print(f"{other._player_name} Heath : {other._health}")
            print(f"{other._player_name} Shield Health : {other._shield}")
        else:
            other.shield = 0
            print("shield Broken")
            other._health -= (self._power)
            print(f"Heath : {other._health}")

    @log_decorator
    def fire_weapon(self,other):
        print(f"{self._player_name} fired {other._player_name}")
        self.take_damage(other)

    def recharge_shield(self):
        pass

class FighterShip(Baseship):
    def __init__(self, Player_name, health = 1000, shield = 500, power= 100):
        super().__init__(Player_name, health, shield, power)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    def special_move(self,other):
        print(f"{self._player_name} used _____ on {other._player_name} ")
        if other._shield < 200:
            other._health -= (self._power)
            print(f"Heath : {other._health}")
            print(f"Shieled Health : {other._shield}")
        else:
            other.shield = 0
            print("shield Broken")
            other._health -= (self._power*2)
            print(f"Heath : {other._health}")
    
class DestroyerShip(Baseship):
    def __init__(self, Player_name, health = 900, shield = 750, power = 130):
        super().__init__(Player_name, health, shield, power)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    def special_move(self,other):
        print(f"{self._player_name} used speacial power (Mega Blast) on {other._player_name}")
        if other._shield < 200:
            other._health -= (self._power)
            print(f"Heath : {other._health}")
            print(f"Shieled Health : {other._shield}")
        else:
            other.shield = 0
            print("shield Broken")
            other._health -= (self._power*2)
            print(f"Heath : {other._health}")

class HybridShip(Baseship):
    def __init__(self, Player_name, health = 1500, shield = 750, power = 170):
        super().__init__(Player_name, health, shield, power)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    def special_move(self, other):
        print(f"{self._player_name} used special power (rapid Blaster) on {other._player_name} ")
        if other._shield < 200:
            other._health -= (self._power)
            print(f"Heath : {other._health}")
            print(f"Shieled Health : {other._shield}")
        else:
            other._shield = 0
            print("shield Broken")
            other._health -= (self._power*2)
            print(f"Heath : {other._health}")   