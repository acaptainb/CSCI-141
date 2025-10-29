import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/student_data.csv"

class Student:
    __slots__ = ('name','id','major','credits')

    
    # name: str
    # id: int
    # major: str
    # credits: int

    def __init__(self, name:str, id:int, major:str):
        self.name = name
        self.id = id
        self.major = major
        self.credits = 0

    def __str__(self)->str:
        return "Name: " + self.name + ", ID: " + str(self.id) + ", Major: " + self.major + ", Credits: " + str(self.credits)
    
    def __repr__(self)->str:
        return str(self)
    
    def add_credits(self, credits:int)->None:
        self.credits += credits

    def __eq__(self, other)->bool:
        # return self.credits == other.credits
        return self.id == other.id
    
    def __lt__(self, other)->bool:
        return self.name < other.name

    def __hash__(self)->int:
        return hash(self.id)

students = []
with open(DATA_FILE) as file:
    next(file)
    for row in file:
        row = row.strip().split(",")
        new_student = Student(row[0],int(row[1]),row[2])
        students.append(new_student)

for student in students:
    print(student)

print("\nGrab a random student and add 4 credits")
rand_student1:Student = random.choice(students)
rand_student1.add_credits(4)
print(rand_student1)

# check two students for equality
rand_student2 = random.choice(students)
rand_student3 = random.choice(students)
print(rand_student2, rand_student3)
print(rand_student2 == rand_student3)

# put the students into a set
student_set = set(students)
print(student_set)

print("\nAdd a random number of credits to all students and then sort the list by credits descending")
for student in students:
    rand_credits = random.randint(1,50)
    student.add_credits(rand_credits)
students.sort()
students.sort(key = lambda student:student.credits, reverse = True)
for student in students:
    print(student)

# Group the students by major, this is on practical exammmmmmm !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
student_dict_by_major = {}
for student in students:
    major = student.major
    if major not in student_dict_by_major:
        student_dict_by_major[major] = []
    student_dict_by_major[major].append(student)

# Show the studets for each major
print("\nStudents grouped by major:")

for major in student_dict_by_major:
    print(major, ":")
    for student in student_dict_by_major[major]:
        print("\t", student)