import json
from datetime import date
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

filepath = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(filepath, "patients.json")

patients_obj = {}

class patients():
      
        def __init__(self, patient_ID, patient_name, patient_age,Admitted_date, patient_ph, patient_gender, patient_address,treatments, status):
                self._patient_ID = patient_ID
                self._patient_name = patient_name
                self._patient_age = patient_age
                self._Admitted_date = Admitted_date
                self._patient_ph = patient_ph
                self._patient_gender = patient_gender
                self._patient_address = patient_address
                self._treatments = treatments
                self._status = status
        
        def add_treatment(self,Treatment):
                self._treatments.append(Treatment)

        def get_treatments_list(self):
                return self._treatments
        
        def update_pati_status(self, status):
               self._status = status
               print("Patient Status Updated")
        
        def patient_status(self):
               print(f"Patient ID : {self._patient_ID}")
               print(f"Patient Name : {self._patient_name}")
               print(f"Patient Status : {self._status}")

        def get_patint_detials(self):
               print(f"""
"Name" : {self._patient_name}
"Age" : {self._patient_age}
"Admitted Date" :{ self._Admitted_date}
"Phone Number" : {self._patient_ph}                  
"Gender" : {self._patient_gender}
"Address" : {self._patient_address}
"Treatments" :{ self._treatments}
"Status" :{ self._status}""")
               

        def to_dict(self):
               return {
                       "Name" : self._patient_name,
                        "Age" : self._patient_age,
                        "Admitted Date" : self._Admitted_date,
                        "Phone Number" : self._patient_ph,                  
                        "Gender" : self._patient_gender,
                        "Address" : self._patient_address,
                        "Treatments" : self._treatments,
                        "Status" : self._status   
                }
        
with open(file, "r", encoding="utf-8") as f:
    patients_dic = json.load(f)
    keys = patients_dic.keys()

    for key in keys:
          patients_obj[key] = patients(key,patients_dic[key]["Name"],patients_dic[key]["Age"], patients_dic[key]["Admitted Date"],patients_dic[key]["Phone Number"],patients_dic[key]["Gender"],patients_dic[key]["Address"],patients_dic[key]["Treatments"], patients_dic[key]["Status"])

p_id = len(patients_dic)

def addpatient():
        Admitted_date = str(date.today())
        patient_id = p_id+1
        patient_name = input("Please enter Patient Name : ")
        patient_age = input("Please Enter Patient age : ")
        patient_ph = input("Please Enter Patient phone number : ")
        patient_gender = input("P{lease enter patient Gender (M/F) : ")
        patient_address = input("Please enter patient Address : ")
        patient_status = input("Please Enter Patient Status: ")
        patients_obj[patient_id] = patients(patient_id, patient_name, patient_age,Admitted_date, patient_ph, patient_gender, patient_address,patient_status)

def patient_exiting():
        patients_write = {}
        for x in patients_obj:
              patients_write[x] = (patients_obj[x]).to_dict()

        with open(file,"w", encoding='utf-8') as f:
                json.dump(patients_write, f, indent= 4)
