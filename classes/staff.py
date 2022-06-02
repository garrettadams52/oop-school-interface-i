#staff.py
import csv
from classes.person import Person
class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        parent_instance = super()
        parent_instance.__init__(name, age, role, password, employee_id)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        filename = '/Users/garrettadams/CodeP/Week2/oop-school-interface-i/data/staff.csv' 
        rows = []

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            
            #make a list of lists
            for j, row in enumerate(csvreader):
                if j > 0:
                    rows.append(row)

        return rows