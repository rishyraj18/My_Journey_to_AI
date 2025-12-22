import os, sys, csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

filepath = os.path.dirname(os.path.abspath(__file__))
datafilepath = os.path.join(filepath, "Employees.csv")

emp_obj = {}

patient_detials_authorized_roles = ["Nurse", "Physician","Receptionist", "Gynecologist", "Orthopedic", "Pediatrician", "Cardiologist", "Neurologist", "Dermatologist" ]
patient_discharge_authorized_roles = ["Receptionist"]
patient_treatment_authorized_roles = ["Physician","Receptionist", "Gynecologist", "Orthopedic", "Pediatrician", "Cardiologist", "Neurologist", "Dermatologist" ]
patient_billing_authorized_roles = ["Accountant"]
employees_administration_roles = ["Admin Officer"]

class Hospital_Employees():

    def __init__(self, Emp_ID, password, Emp_Name, Emp_DOB, Emp_phonenumber, Emp_Type, Emp_Addr, Emp_Designation, Emp_Department, Emp_salary, Doctor):
        self._Emp_ID = Emp_ID
        self._password = password
        self._Emp_Name = Emp_Name
        self._Emp_DOB = Emp_DOB
        self._Emp_phonenumber = Emp_phonenumber
        self._Emp_Type = Emp_Type
        self._Emp_Addr = Emp_Addr
        self._Emp_Designation = Emp_Designation
        self._Emp_Department = Emp_Department
        self._Emp_salary = Emp_salary
        self._doctor = Doctor

    def to_dict(self):
        return {
            "Emp_ID": self._Emp_ID,
            "Password": self._password,
            "Emp_Name": self._Emp_Name,
            "Emp_DOB": self._Emp_DOB,
            "Emp_PhoneNumber": self._Emp_phonenumber,
            "Emp_Type": self._Emp_Type,
            "Emp_Address": self._Emp_Addr,
            "Emp_Designation": self._Emp_Designation,
            "Emp_Department": self._Emp_Department,
            "Emp_Salary": self._Emp_salary,
            "Doctor" : self._doctor
        }
    
    def password(self):
        return self._password

    def emp_designation(self):
        return self._Emp_Designation
  
    def change_password(self, new_password):
        self._password = new_password

    def change_phonenumber(self, new_phonenumber):
        self._Emp_phonenumber = new_phonenumber

    def change_designation(self, new_designation):
        self._Emp_Designation = new_designation
    
    def change_department(self, new_department):
        self._Emp_Department = new_department

    def change_address(self, address):
        self._Emp_Addr = address

with open(datafilepath, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp = row["Emp_ID"]
        emp_obj[emp] = Hospital_Employees(
            row["Emp_ID"],
            row["Password"],
            row["Emp_Name"],
            row["Emp_DOB"],
            row["Emp_PhoneNumber"],
            row["Emp_Type"],
            row["Emp_Address"],
            row["Emp_Designation"],
            row["Emp_Department"],
            row["Emp_Salary"],
            row["Doctor"]
        )

def create_new_employee():
    Emp_ID = input("Please Enter New Emp ID : ")
    password = input("Create new Password : ")
    Emp_Name = input("New Employee Name : ")
    Emp_DOB = input("Enter Employee DOB : ")
    Emp_phonenumber = input("Enter Employee PhoneNumber : ")
    Emp_Type = input("Enter Employee Type (Doctor/Receptionist/Accoutant/Management) : ")
    Emp_Addr = input("Enter Employee Address : ")
    Emp_Designation = input("Enter Employee Designation : ")
    Emp_Department = input("Enter Employee Department : ")
    Emp_Salary = input("Enter Salary For the Employee : ")
    Doctor = input("Is the Employee Doctor? : ")
    emp_obj[Emp_ID] = Hospital_Employees(Emp_ID,password, Emp_Name, Emp_DOB, Emp_phonenumber, Emp_Type, Emp_Addr, Emp_Designation, Emp_Department, Emp_Salary, Doctor)

def employee_exiting():
    with open(datafilepath, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ["Emp_ID", "Password", "Emp_Name", "Emp_DOB", "Emp_PhoneNumber",
                    "Emp_Type", "Emp_Address", "Emp_Designation", "Emp_Department", "Emp_Salary", "Doctor"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for emp in emp_obj.values():
            writer.writerow(emp.to_dict())

