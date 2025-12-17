import json, csv, os, sys
from datetime import date

mainpath = os.path.dirname(os.path.abspath(__file__))

trip_csv = os.path.join(mainpath, "data", "trips.csv")
Hotels_csv = os.path.join(mainpath, "data", "preferences.json")
logs_txt = os.path.join(mainpath, "data", "logs.txt")

with open(trip_csv, 'r', encoding = "utf-8") as f:
    trip_temp = json.load(f)


print("-----------------------Welcome to Trip Planner-----------------------\n\n")

main_menu1 = 0
while main_menu1 != 0:
    print("Main Menu :-")
    print("""
    1. Plan a Travel
    2. Get Saved the Trip plans
    3. Save a preference
    4. Exit
    """)
    main_menu1 = input("Please select an option (1/2/3/4): ")

    match main_menu1:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Exiting Travel Planner........")
        case _:
            print("Invalid Input!, Please select the correct option")

def plan_a_travel:
    Print("-------------Planning a Travel---------------")
    print("Please set you preferences:")
    trip_destination = input("Please enter you Travel Destination : ")
    trip_Budget = int(input("Please enter your budget for the trip : "))
    no_of_days = int(input("Please Enter no of days : "))
    start_date = ("Please enter the planned start Date (DD-MM-YYYY) : ")