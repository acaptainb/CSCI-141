import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/student_data.csv"

students = []
with open(DATA_FILE) as file:
    next(file)
    for row in file:
        row = row.strip().split(",")
        new_student = [row[0],int(row[1]),row[2], 0]
        students.append(new_student)

def print_student(student:list)->None:
    print("Name: ", student[0], ", ID:", student[1], ", Major:", student[2], ", Credits", student[3])

def add_credits(student:list, credits:int)->None:
    student[3] += credits

for student in students:
    print_student(student)

print("\nGrab a random student and add 4 credits")
rand_student = random.choice(students)
add_credits(rand_student, 4)
print_student(rand_student)
