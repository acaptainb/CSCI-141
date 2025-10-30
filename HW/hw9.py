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

    def __init__(self, max_pass):
        self.max_pass = max_pass
        self.passengers = 0
        self.inflight = False

    def load(self, newpass: int):
        if self.passengers+ newpass <= self.max_pass:
            self.passengers+=newpass
        else:
            self.passengers = self.max_pass

        return self.passengers
    def takeoff(self):  
        if self.inflight or self.passengers == 0 :
            return False
        else:
            self.inflight = True
            return True

    def __str__(self):
        return "Plane has " + str(self.passengers) + " out of " + \
            str(self.max_pass) + " on board and is" + \
            (" " if self.inflight else " not ") + "in flight"

def most_legs(zoo):
    legs_list = [animal.legs for animal in zoo]
    most_legs_num = max(legs_list)
    for animal in zoo:
        if animal.legs == most_legs_num:
            return animal.species


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

