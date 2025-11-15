from modules.grading_system import GradingSystem
from modules.course import course

class student(GradingSystem):

    def __init__(self, name, roll_no, course, mark = None, attendance = 0, grade = None):
        self.__name = name.title()
        self.__roll_no = roll_no
        self.__course = course
        self.__mark = mark
        self.__attendance = attendance
        self.__grade = grade
        print("Student Record created")
        print(f"Student Name: {self.__name}\nRoll No: {self.__roll_no}\nCourse: {self.__course}")

    def update_name(self,name):
        temp_name = self.__name
        self.__name = name.title()
        print(f"Student name changed from {temp_name} to {self.__name}")

    def update_course(self,c_name):
        temp_name = self.__course
        self.__course = c_name.title()

    def update_marks(self,n_mark):
        self.__mark = n_mark
        print("Mark Updated for the student")

    def update_attendance(self,attendance):
        self.__attendance = attendance
        print("Attendance updated for the student")

    def display_info(self):
        print(f"Student name: {self.__name}\nRoll No: {self.__roll_no}\nCourse :{self.__course}\nMark scored: {self.__mark}\nAttendance: {self.__attendance}")

    def calculate_grade(self):
        if 0 < self.__mark != None:
            if self.__mark >= 90:
                self.__grade = "A"
            elif self.__mark >= 80:
                self.__grade = "B"
            elif self.__mark >= 70:
                self.__grade = "C"
            elif self.__mark >= 40:
                self.__grade = "D"
            else:
                self.__grade = "E"

            print(f"The Grade of the Student is {self.__grade}")   
        else:
            print("Grade Not Updated in the record")

    def __lt__(self,other):
        return self.__mark > other.__mark

    def __str__(self):
        return (f"Student name: {self.__name}\nRoll No: {self.__roll_no}\nCourse :{self.__course}\nMark scored: {self.__mark}\nAttendance: {self.__attendance}")