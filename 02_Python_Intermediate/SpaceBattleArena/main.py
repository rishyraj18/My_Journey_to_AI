from ships import FighterShip, DestroyerShip, HybridShip
from weapons import Laser_Weapon, Plasma_Weapon
from utility import log_decorator

print("Welcome come to Space Battle Arena")

i = None
players = {}
players_weapons = {}
while i != 6:
    print("Main Menu:-\n"
      "1. Create Player\n"
      "2. Attack Player\n"
      "3. Use Special Power\n"
      "4. Get Shield\n"
      "5. Get Health\n"
      "6. Exit")

    i = int(input("Please Select the an Option: "))
        
    match i:
        case 1:
            p_name = str(input("Please Enter Player Name: "))
            print("Please select the Type of chip:\n1.Fighter Ship\n2.Destroyer Ship\n3.Hybrid Ship")
            ship = int(input("Type of Ship: "))
            print("Please select your special Weapon:\n1.Laser Weapon\n2.Plasma Weapon")
            weapon = int(input("Type is Weapon: "))
            if ship == 1:
                if weapon == 1:
                    players[p_name] = FighterShip(p_name)
                    players_weapons[p_name] = Laser_Weapon(p_name)
                elif weapon == 2:
                    players[p_name] = FighterShip(p_name)
                    players_weapons[p_name] = Plasma_Weapon(p_name)
                else:
                    print("Wrong Option Selected\nUnable to create the player")
            elif ship == 2:
                if weapon == 1:
                    players[p_name] = DestroyerShip(p_name)
                    players_weapons[p_name] = Laser_Weapon(p_name)
                elif weapon == 2:
                    players[p_name] = DestroyerShip(p_name)
                    players_weapons[p_name] = Plasma_Weapon(p_name)
                else:
                    print("Wrong Option Selected\nUnable to create the player")
            elif ship == 3:
                if weapon == 1:
                    players[p_name] = HybridShip(p_name)
                    players_weapons[p_name] = Laser_Weapon(p_name)
                elif weapon == 2:
                    players[p_name] = HybridShip(p_name)
                    players_weapons[p_name] = Plasma_Weapon(p_name)
                else:
                    print("Wrong Option Selected\nUnable to create the player")
            else:
                    print("Wrong Option Selected\nUnable to create the player")
        case 2:
            atck_player = str(input("Please enter the Player name attacking: "))
            other_player = str(input("Please enter the player your Attacking: "))
            players[atck_player].fire_weapon(players[other_player])

        case 3:
            print(players)
            print(players_weapons)
            
print("Exiting The Game")