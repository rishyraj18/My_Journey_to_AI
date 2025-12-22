import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.exceptions import Invalid_Patient, Invalid_Doctor, Invalid_Treatment, Invalid_username, Invalid_password
from Patients.patient import patients_obj
from Employees.Employees import emp_obj
from Accounting.Accounting import treatments



def patient_id_validation(P_id):
    if P_id in patients_obj.keys():
        pass
    else:
        raise Invalid_Patient()

def doctor_validation(d_id):
    if d_id in emp_obj.keys():
        pass
    else:
        raise Invalid_Doctor()

def treatment(treatment):
    if treatment in treatments:
        pass
    else:
        raise Invalid_Treatment()
    

def login_validation(u_name, password):
    if u_name in emp_obj.keys():
        if password == emp_obj[u_name].password():
            print("Login Successfull")
        else:
            raise Invalid_password()
    else:
        raise Invalid_username()
    