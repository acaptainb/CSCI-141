from dataclasses import dataclass

@dataclass
class Student:
    name: str
    id: int
    major: str
    credits: int


print(Student)
