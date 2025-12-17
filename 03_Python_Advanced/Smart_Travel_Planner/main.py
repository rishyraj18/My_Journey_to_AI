import json, csv, os, sys

mainpath = os.path.dirname(os.path.abspath(__file__))

trip_csv = os.path.join(mainpath, "data", "trips.csv")
prefernces_json = os.path.join(mainpath, "data", "preferences.json")
logs_txt = os.path.join(mainpath, "data", "logs.txt")

with open(trip_csv, 'r', encoding = "utf-8") as f:
    trip_temp = json.load(f)
    

print("-----------------------Welcome to Trip Planner-----------------------\n\n")

main_menu1 = 0
while main_menu1 != 0:
    print("Main Menu :-")
    print("""
    1. Plan a Travel
    2. Get saved preferences
    3. Get Saved the Trip plans
    4. Save a preference
    5. Exit
    """)
    main_menu1 = input("Please select an option (1/2/3/4/5): ")

    match main_menu1:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Exiting Travel Planner........")
        case _:
            print("Invalid Input!, Please select the correct option")
            