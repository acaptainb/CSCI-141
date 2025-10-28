import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/student_data.csv"

from dataclasses import dataclass

@dataclass(frozen=False, slots = True)
class Student:
    name: str
    id: int
    major: str
    credits: int

students = []
with open(DATA_FILE) as file:
    next(file)
    for row in file:
        row = row.strip().split(",")
        new_student = Student(row[0],int(row[1]),row[2], 0)
        students.append(new_student)

# Don't need this now because dataclass objects have a built in str representation of themselves
# def print_student(student:list)->None:
#     print("Name: ", student[0], ", ID:", student[1], ", Major:", student[2], ", Credits", student[3])

def add_credits(student:Student, credits:int)->None:
    # student.creditss += credits  having slots = True prevents us from screwing up a field name or adding other random fields to a specific instance
    student.credits += credits

for student in students:
    print(student)

print("\nGrab a random student and add 4 credits")
rand_student = random.choice(students)
add_credits(rand_student, 4)
print(rand_student)
