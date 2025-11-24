from modules.student import student
from modules.course import course
from Utility.decorators import validate_input , log_action, performance_check
from Utility.validators import validate_mark, validate_name, validate_roll


print("Hi, Welcome to EduTrack_Student_report_tracker")



inp = None
student_ID = {}
course_ID = {}
while inp != 0:
    print("select One Option from below")
    print("1. Add Student\n"
    "2. Edit Student Name\n"
    "3. Add Course\n"
    "4.Add Topics to a Course\n"
    "5. Remove Student\n"
    "6. Update Marks\n"
    "7. Update Attendance\n"
    "8. View Student Details\n"
    "9. View All Students\n"
    "0. Exit")

    inp = int(input("Please the Number: "))

    match inp:
            case 1:
                print("Give the below Details for student registeration")
                std_id = input("Please enter student ID: ")
                name = input("Please enter student name: ")
                roll_no = int(input("Please enter Roll_no: "))
                course_name = input("Please Enter Course name:")
                student_ID[std_id] = student(name, roll_no, course_name)

            case 2:
                std_id = input("Please enter student_ID to change the details: ")
                n_name = input("Please Enter the Name: ")
                if std_id in student_ID:
                    if validate_name(n_name):
                        (student_ID[std_id]).update_name(n_name)
                    else:
                        print("Name Format Missmatch")
                else:
                    print("Unable to Find Student Details\n Returned to Main Menu\n")

            case 3:
                course_id = input("Please Enter Course ID: ")
                course_name = input("Please Enter Course Name: ")
                course_duration = input("Please Enter the Course Duration: ")
                if course_id not in course_ID:
                    course_ID[course_id] = course(course_name, course_duration)
                else:
                    print("Course ID already Exists")

            case 4:
                course_id = input("Please Enter Course ID: ")
                topics = input("Please Enter the topics need to be added: ")
                course_ID[course_id].add_topic(topics)

            case 5:
                std_id = input("Please enter student_ID to Remove: ")
                if std_id in student_ID:
                    del student_ID[std_id]
                    print(student_ID)
                else:
                    print("Unable to Find Student Details\n Returned to Main Menu\n")

            case 6:
                std_id = input("Please enter student_ID to update Marks: ")
                marks = int(input("Please enter marks: "))
                if std_id in student_ID:
                    student_ID[std_id].update_marks(marks)
                else:
                    print("Unable to Find Student Details\n Returned to Main Menu\n")
 
            case 7:
                std_id = input("Please enter student_ID to update Attendance: ")
                attendance = int(input("Please enter attendance: "))
                if std_id in student_ID:
                    student_ID[std_id].update_attendance(attendance)
                else:
                    print("Unable to Find Student Details\n Returned to Main Menu\n")

            case 8:
                std_id = input("Please enter student_ID to view details: ")
                if std_id in student_ID:
                    student_ID[std_id].display_info()
                else:
                    print("Unable to Find Student Details\n Returned to Main Menu\n")
 
            case 9:
                print("List of all students")
                for std_id in student_ID:
                    student_ID[std_id].view_names()
            
            case 0:
                pass

            case _:
                print("Please Enter Correct option")
    
print("Exiting EduTracker Module")