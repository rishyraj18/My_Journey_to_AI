# A simple Python game simulation using OOP with Warrior, Mage, and Archer classes,
# featuring attacks, health tracking, and multiple battle rounds.

class character:                                            #Parent Class                                               
    def __init__(self, player_name, player_health, player_attack_power):
        self.player_name = player_name
        self.__player_health = player_health
        self.__player_attack_power = player_attack_power

    def attack(self, target):                               # Attack Class
        if target.__player_health > 0:
            target.__player_health -= self.__player_attack_power
            print(f"{target.player_name} is attacked by {self.player_name}")
        else:
            print("Player is Already Dead")

    def is_alive(self):
        if self.__player_health >0 :
            print("player is alive")
        else:
            print("Player is dead")

    def get_health(self):
        print(f"Player Health: {self.__player_health}")
            
class warrior(character):
    def __init__(self, player_name, player_health = 150, player_attack_power =  25):
        super().__init__(player_name, player_health, player_attack_power)

    def attack(self, player_attacked):
        super().attack(player_attacked)
        

class Mage(character):

    def __init__(self, player_name, player_health = 90, player_attack_power = 40):
        super().__init__(player_name, player_health, player_attack_power)

    def attack(self, player_attacked):
        super().attack(player_attacked)
    
class Archer(character):
    def __init__(self, player_name, player_health  = 90, player_attack_power = 40):
        super().__init__(player_name, player_health, player_attack_power)

    def attack(self, player_attacked):
        super().attack(player_attacked)

p1 = warrior("Rishy")
p2 = Mage("Rocky")
p3 = Archer("Simba")

p1.attack(p2)
p2.attack(p3)
p3.attack(p1)

print("\n--- 📊 Status After Round 1 ---")
p1.get_health()
p2.get_health()
p3.get_health()

p1.attack(p2)
p2.attack(p3)
p3.attack(p1)

print("\n--- 📊 Status After Round 2---")
p1.get_health()
p2.get_health()
p3.get_health()