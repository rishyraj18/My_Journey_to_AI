from ships import FighterShip, DestroyerShip, HybridShip
from weapons import Laser_Weapon, Plasma_Weapon
from utility import log_decorator

print("Welcome come to Space Battle Arena")

i = None
players = {}
players_weapons = {}
while i != 8:
    print("Main Menu:-\n"
      "1. Create Player\n"
      "2. Attack Player\n"
      "3. Use Special Power\n"
      "4. Recharge Shield\n"
      "5. Restore health\n"
      "6. Get Shield\n"
      "7. Get Health\n"
      "8. Exit")

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
            if atck_player in players and other_player in players:
                players[atck_player].fire_weapon(players[other_player])
            else:
                print("Wrong Player name entered")
        case 3:
            atck_player = str(input("Please enter the Player name attacking: "))
            other_player = str(input("Please enter the player your Attacking: "))
            if atck_player in players and other_player in players:
              if players[atck_player]._shield > 200:
                  print(f"{players[atck_player]._player_name} used speacial power (Mega Blast) on {players[other_player]._player_name}")
                  players[other_player]._health -= round((players_weapons[atck_player]._damage))
                  players[other_player]._shield -= round((players_weapons[atck_player]._damage) / 2)
                  print(f"{players[other_player]._player_name} Heath : {players[other_player]._health}")
                  print(f"{players[other_player]._player_name} Shield Health : {players[other_player]._shield}")
              else:
                  players[atck_player]._shield = 0
                  print("shield Broken")
                  players[atck_player]._health -= (players_weapons[other_player]._damage)
                  print(f"{players[other_player]._player_name} Heath : {players[other_player]._health}")
                  print(f"{players[other_player]._player_name} Shield Health : {players[other_player]._shield}")
            else:
                print("Wrong Player name entered")
        case 4:
            rechg_player = str(input"Please enter player shiled need to be recharged: ")
            if rechg_player in players:
                players[rechg_player].recharge_shield()
            else:
                print("Wrong Player name entered")
        case 5:
            rstr_player = str(input("Please enter the player name to restore health: "))
             if rechg_player in players:
                players[rstr_player].restore_health()
            else:
                print("Wrong Player name entered")
        case 6:
            player_name= str(input("Please enter the player name to get shield: "))
            if player_name in players:
                print(str(players[player_name]))
            else:
                print("Wrong Player name entered")
        case 7:
            player_name= str(input("Please enter the player name to get Health: "))
            if player_name in players:
                print(len(players[player_name]))
            else:
                print("Wrong Player name entered")
        case _:
            print("Wrong option selected,Please select correct option")

print("Exiting The Game")