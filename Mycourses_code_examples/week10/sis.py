'''
Dataclass example for CSCI-141
@author RIT CS
'''
import csv
import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/student_data.csv"

from dataclasses import dataclass

@dataclass(frozen=True, slots = True)
class Student:
    name: str
    id: int
    major: str

@dataclass (slots = True)
class Course:
    dept: str
    number: int
    students: list[Student]

def main():
    courses = [Course('CSCI',141,[]), Course('CSCI',140,[]), Course('MATH',100,[])]

    students = []
    with open(DATA_FILE) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            new_student = Student(row[0],int(row[1]),row[2])
            students.append(new_student)
    students_copy = students.copy()

    # randomly add the students to a course
    while len(students_copy):
        rand_course = random.choice(courses)
        random_student = students_copy.pop(random.randrange(len(students_copy)))
        rand_course.students.append(random_student)

    # show where everybody ended up
    print("Courses and which students are taking them:")
    for course in courses:
        print(course.dept, course.number)
        for student in course.students:
            print("\t", student)
        print()
    print()

    # Group the students by major
    student_dict_by_major = {}
    for student in students:
        major = student.major
        if major not in student_dict_by_major:
            student_dict_by_major[major] = []
        student_dict_by_major[major].append(student)
    
    # Show the studets for each major
    print("Students grouped by major:")

    for major in student_dict_by_major:
        print(major, ":")
        for student in student_dict_by_major[major]:
            print("\t", student)

if __name__ == '__main__':
    main()
    