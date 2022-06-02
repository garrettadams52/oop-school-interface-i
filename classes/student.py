# student.py
from classes.person import Person
import csv
class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        parent_instance = super()
        parent_instance.__init__(name, age, role, password, school_id)
        self.school_id = school_id


    @classmethod
    def all_students(cls):
        filename = '/Users/garrettadams/CodeP/Week2/oop-school-interface-i/data/students.csv' 
        rows = []
       
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            #make a list of lists
            for j, row in enumerate(csvreader):
                if j > 0:
                    rows.append(row)
                elif j == 0:
                    keys = row

        return [dict(zip(keys, i)) for i in rows]