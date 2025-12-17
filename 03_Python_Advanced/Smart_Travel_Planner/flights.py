import os
import csv
from abc import ABC, abstractmethod

currentdirpath = os.path.dirname(os.path.abspath(__file__))
flights_csv = os.path.join(currentdirpath, "data", "flight.csv")

flights_obj = {}

class Flights(ABC):
    def __init__ (self, flight_number, origin, destination, price, date, f_type):
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._price = price
        self._date = date
        self._ftype = f_type
    
    def to_dict(self):
        return{
            "flight_number" : self._flight_number,
            "origin" : self._origin,
            "destination" : self._destination,
            "price" : self._price,
            "date" : self._date,
            "f_type" : self._ftype
        }
    
    def __str__(self):
        return (f"""---------Flight Details----------
        Flight Number : {self._flight_number}
        Flight Origin : {self._origin}
        Flight Destination : {self._destination}
        Flight Ticket Price : {self._price}
        Fligth Boarding Date : {self._date}
        Flight Type : {self._ftype}""")

    @abstractmethod
    def book_flight(self):
        pass

    @abstractmethod
    def cancel_flight(self):
        pass

class DomesticFlight(Flights):

    def __init__(self, flight_number, origin, destination, price, date, ftype = "Domestic"):
        super().__init__(flight_number, origin, destination, price, date, ftype)

    def book_flight(self):
        print(self)
        confirmation = input("Do you want to proceed (Y/N)? : ")
        if confirmation == "Y":
            print("Booking Confirmed")
        else:
            print("Booking Not Confirmed")

class InternationalFlights(Flights):
    def __init__(self, flight_number, origin, destination, price, date, ftype = "International"):
        super().__init__(flight_number, origin, destination, price, date, ftype)

    def book_flight(self):
        print(self)
        confirmation = input("Do you want to proceed (Y/N)? : ")
        if confirmation == "Y":
            confirmation2 = input("Please Confirm do you have a passport with valid Visa for your destination? : ")
            if confirmation2 == "Y":
                print("Booking Confirmed")
            else:
                print("Booking Not Confirmed")
        else:
            print("Booking Not Confirmed")

    def cancel_flight(self):
        confirmation = input("Do you need cancel the flight (Y/N)? : ")
        if confirmation == "Y":
            print("Booking Canceled")
        else:
            print("Booking not Canceled")


with open(flights_csv, "r", encoding = "utf-8") as f:
    flight_csv = DictReader(f)
    for row in flight_csv:
        flightnum = row["flight_number"]
        if row["f_type"] == "Domestic":
            flights_obj[flightnum] = DomesticFlight(row["flight_number"], row["origin"], row["destination"], row["price"], row["date"], row["f_type"])
        else:
            flights_obj[flightnum] = InternationalFlights(row["flight_number"], row["origin"], row["destination"], row["price"], row["date"], row["f_type"])

def exit():
    with open(flight_csv, "w", encoding = "utf-8", newline = "") as f:
        fieldnames = ["flight_number","origin","destination","price","date","f_type"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        for flight in flights_obj.values():
            writer.writerow(flight.to_dict())
        
