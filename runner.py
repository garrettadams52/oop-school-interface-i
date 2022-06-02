from classes.school import School 
from classes.student import Student
from classes.staff import Staff
from classes.person import Person

school = School('Ridgemont High') 
student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
student1 = Student(**student_info)
options = [1,2,3,4,5]

# print(school.name, student1.school_id)
# print(Student.all_students())
# print(Staff.all_staff())

#get input
sel = int(input('''
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit\n'''))

#check valid input
while(sel not in options):
    sel = int(input('Please select from options 1-5\n'))

#return info
if sel == 1:
    print(school.students)
elif sel == 2:
    id = input('Enter the student id ')
    check = next((item for item in school.students if item["school_id"] == id), "There is no student with that id")
    print(check)
#elif sel == 3:

