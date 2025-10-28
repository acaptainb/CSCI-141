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

    # add your code here

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

