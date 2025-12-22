import sys
import os
import csv
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Employees.Employees import Hospital_Employees, create_new_employee,employee_exiting,emp_obj, employees_administration_roles,patient_detials_authorized_roles, patient_treatment_authorized_roles, patient_discharge_authorized_roles,patient_billing_authorized_roles
from Patients.patient import patients, addpatient, patients_obj, patient_exiting
from Utilities.validations import login_validation, patient_id_validation, treatment
from Utilities.exceptions import Invalid_username, Invalid_password, Invalid_Patient, Invalid_Treatment
from Accounting.Accounting import calulating_patient_bill


print("----------------------------------------Welcome to Login Management System----------------------------------------")

useranme = None
userdesignation = None

def module_exit():
    employee_exiting()
    patient_exiting()
    exit
    

def mainmenu():
    
    mainmenu_input = None
    while mainmenu_input != 0:
        print("\n\n-------------------------Main Menu----------------------------------------")
    
        print("""
1. Add New Patient
2. Patient Status Check
3. Get Patient Details
4. Add Treatment to the Patient
5. Discharge a Patient
6. Admitt Discharged Patient
7. Calculate Patient Bill
8. User Profile Management
9. Admin Controlls
0. Exit""")

        mainmenu_input = int(input("Please select your option : "))

        match mainmenu_input:
            case 1:
                if userdesignation == "Receptionist":
                    addpatient()
                else:
                    print("You don't have permission to admit a patient")
            case 2:
                if userdesignation in patient_detials_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    try: 
                        patient_id_validation(patient_id)
                    except Invalid_Patient as e:
                        print(f"Error !! - {e}")
                    else:
                        patients_obj[patient_id].patient_status()
                else:
                    print("You Dont Have permission to check patient details")
            case 3:
                if userdesignation in patient_detials_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    try: 
                        patient_id_validation(patient_id)
                    except Invalid_Patient as e:
                        print(f"Error !! - {e}")
                    else:
                        print(patients_obj[patient_id].get_patint_detials())
                else:
                    print("You Dont Have permission to check patient details")
            case 4:
                if userdesignation in patient_treatment_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    treatment_inp = input("Please enter Treatment Name : ")
                    try: 
                        patient_id_validation(patient_id)
                        treatment(treatment_inp)
                    except (Invalid_Patient, Invalid_Treatment) as e:
                        print(f"Error !! - {e}")
                    else:
                        patients_obj[patient_id].add_treatment(treatment)
                else:
                    print("You Dont have permission to Add Treatments to the patients")
            case 5:
                if userdesignation in patient_discharge_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    try: 
                        patient_id_validation(patient_id)
                    except Invalid_Patient as e:
                        print(f"Error !! - {e}")
                    else:
                        patients_obj[patient_id].update_pati_status("Discharged")
                else:
                    print("You Dont have permission to Discharge patients")
            case 6:
                if userdesignation in patient_discharge_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    try: 
                        patient_id_validation(patient_id)
                    except Invalid_Patient as e:
                        print(f"Error !! - {e}")
                    else:
                        patients_obj[patient_id].update_pati_status("Admitted")
                else:
                    print("You don't Have permission to Addmit a patient Again")
            case 7:
                if userdesignation in patient_billing_authorized_roles:
                    patient_id = input("Please enter patient ID : ")
                    try: 
                        patient_id_validation(patient_id)
                    except Invalid_Patient as e:
                        print(f"Error !! - {e}")
                    else:
                        calulating_patient_bill(patient_id)
                else:
                    print("Access Denied")     
            case 8:
                print("--------------------------User Profile Management-----------------------")
                userprofileinput = None
                while userprofileinput != 0:
                    print("""
1. Change Password
2. Change Phone Number
3. Change Address
0. Exit""")
                    userprofileinput = int(input("Please select an option : "))
                    match userprofileinput:
                        case 1:
                            print("\n\nPassword Update\n")
                            password = input("Please enter new password : ")
                            emp_obj[u_name].change_password(password)
                            print("\nPassword Changed successfully")
                        case 2:
                            print("\n\nPhone Number Update\n")
                            phonenumber = int(input("Please enter you new Phone Number : "))
                            emp_obj[u_name].change_phonenumber(phonenumber)
                            print("\nPhone Number changed Successfully")
                        case 3:
                            print("\n\nAddress Update\n")
                            address = input("Please enter new address : ")
                            emp_obj[u_name].change_address[address]
                            print("\nAddress Changed Successfully")
                        case 0:
                            mainmenu()
                        case _:
                            print("Please select correct option")
            case 9:
                if userdesignation in employees_administration_roles:
                    useradministaration = None
                    while userdesignation != 0:
                        print("User Administration")
                        print("""
1. Add New Employee
2. Change Employee Desgination
3. Change Employee Department
0. Exit""")
                   
                        useradministaration = int(input("Please select an option"))
                        match userdesignation:
                            case 1:
                                create_new_employee()
                            case 2:
                                user_id = input("Please enter User ID : ")
                                Designation = input("Please enter user designation : ")
                                emp_obj[user_id].change_designation(Designation)
                                print("User Designation Changes Successfully")
                            case 3:
                                user_id = input("Please enter User ID : ")
                                Department = input("Please enter user department : ")
                                emp_obj[user_id].change_department(Department)
                                print("User Department Changes Successfully")
                            case 0:
                                mainmenu()
                            case _:
                                print("Please select correct Option = ")
            case 0:
                module_exit()
            case _:
                print("Please select correct option : ")
    
input1 = None
def initialization():
    print("""
        1. Employee Login
        2. Exit
    """)
    global input1
    input1 = int(input("Please Enter your option : "))


while input1 != 2:
    initialization()

    if input1 == 1:
        print("Employee Login Selected")
        try:
            u_name = input("Please enter you username : ")
            u_password = input("Please enter you password : ")
            login_validation(u_name, u_password)
        except (Invalid_username, Invalid_password) as e:
            print(f"Error Message : {e}")
        else:
            useranme = u_name
            userdesignation = emp_obj[u_name].emp_designation()
            print(useranme)
            print(userdesignation)
            mainmenu()
            break
    elif input1 == 2:
        module_exit()
        print("Exiting...")
    else:
        print("\nPlease select correct option!!\n")