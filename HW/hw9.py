'''
CSCI-141 Homework 9
@author RIT CS
@author Abdulaziz
'''

from dataclasses import dataclass

@dataclass
class Animal:
    species: str
    weight: float
    legs: int

class Airplane:
    inflight: bool
    max_pass: int
    passengers: int

    def __init__(self, passengers, max_pass, inflight):
        self.max_pass = max_pass
        self.passengers = passengers
        self.inflight = inflight

    def load(self, newpass: int):
        pass
    def takeoff(self):  
        pass

    # add your code here

def most_legs(zoo):
    legs_list = [animal.legs for animal in zoo]
    most_legs_num = max(legs_list)
    for animal in zoo:
        if animal.legs == most_legs_num:
            return animal.species

    def __str__(self):
        return "Plane has " + str(self.passengers) + " out of " + \
            str(self.max_pass) + " on board and is" + \
            (" " if self.inflight else " not ") + "in flight"

def plane_test():
    plane = Airplane(120)
    print(plane.takeoff())
    res = plane.load(50)
    print(plane)
    res = plane.load(100)
    plane.takeoff()
    print(plane)

if __name__ == '__main__':
    plane_test()

