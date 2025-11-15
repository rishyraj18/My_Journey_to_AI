from modules.student import student
from modules.course import course
from Utility.decorators import validate_input , log_action, performance_check
from Utility.validators import validation


print("Hi, Welcome to EduTrack_Student_report_tracker")
print("select One Option from below")
print("1. Add Student\n"
    "2. Edit Student Name\n"
    "3. Add Course\n"
    "4. Enroll Student in Course\n"
    "5. Update Marks\n"
    "6. Update Attendance\n"
    "7. View Student Details\n"
    "8. View All Students\n"
    "9. Exit")

inp = int(input("Please the Number: "))

if inp != 9:
    match inp:
        case 1:
            print("Give the below Details for student registeration")
            std_id = input("Please enter the student ID: ")
            name = input("Please enter student name: ")
            roll_no = int(input("Please enter Roll_no: "))
            course_name = input("Please Enter Course name: ")
            std_id = student(name, roll_no, course_name)
        case 2:
            std_id = input("Please the student_ID to change the details")
            n_name = input("Please Enter the Name: ")
else:
    print("Exiting EduTracker Module")



