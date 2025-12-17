from datetime import date
import os, json, sys, csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.logging_decorator import logging_decorator
from Patients.patient import patients_dic


dirpath = os.path.dirname(os.path.abspath(__file__))
price_catalog = os.path.join(dirpath, "Treatment_Price.csv")

Catalog_price = {}

with open(price_catalog, "r", encoding='utf-8') as f:
    csv_price = csv.DictReader(f)
    for row in csv_price:
        Catalog_price[row["treatment_tests"]] = row["price"]

