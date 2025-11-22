from abc import ABC, abstractmethod
from utility import log_decorator, cooldown

class Baseship(ABC):
    def __init__(self, Player_name,health, shield, power,life):
        self._player_name = Player_name
        self._health = health
        self._shield = shield
        self._power = power
        self._life = life

    
    @abstractmethod
    def recharge_shield(self):
        pass
        
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
        print(f"rechargeing Shield for {self._player_name}")
        self._shield = min(self._shield + (self._shield /10), 750)
        print(f"shield recharged\nShield power : {self._shield}")
    
    def __str__(self):
        return f"Sheld Power remaning for the player {self._player_name}: {self._shield}"
    
    def __len__(self):
        return self._shield

class FighterShip(Baseship):
    def __init__(self, Player_name, health = 1000, shield = 750, power= 100,life = 3):
        super().__init__(Player_name, health, shield, power,life)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    @cooldown(30)
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

    def restore_health(self):
        if self._life > 0:
            print(f"Restoring health for player {self._player_name}")
            self._life -= 1
            self._health = 1000
        else:
            print("You have no lifes left")
    
class DestroyerShip(Baseship):
    def __init__(self, Player_name, health = 900, shield = 750, power = 130, life = 3):
        super().__init__(Player_name, health, shield, power,life)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    @cooldown(30)
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

    def restore_health(self):
        if self._life > 0:
            print(f"Restoring health for player {self._player_name}")
            self._life -= 1
            self._health = 900
        else:
            print("You have no lifes left") 

class HybridShip(Baseship):
    def __init__(self, Player_name, health = 1200, shield = 750, power = 90,life=3):
        super().__init__(Player_name, health, shield, power,life)
        print(f"{self._player_name} Player created\nHealth: {self._health}\nShield Strenght: {self._shield}\nFire Power: {self._power}" )

    @cooldown(30)
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
    
    def restore_health(self):
        if self._life > 0:
            print(f"Restoring health for player {self._player_name}")
            self._life -= 1
            self._health = 1200
        else:
            print("You have no lifes left")
    