'''
Dataclass example for CSCI-141
@author RIT CS
'''
import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/car_data.csv"

from dataclasses import dataclass

""" Define the car dataclass
"""
@dataclass (frozen = False, slots = False)
class Car:
    model: str
    tanksize: float
    fuel: float
    mpg: float
    miles: float

def drive(car:Car, distance:float)->None:
    if distance > 0:
        car.miles += distance
        car.fuel -= distance/car.mpg

def main():
    """ Create a list of cars from the provided datafile
    """
    cars = []
    with open(DATA_FILE) as file:
        next(file)
        for row in file:
            row = row.strip().split(",")
            new_car = Car(row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]))
            cars.append(new_car)

    """ Pick a random car and do some stuff to it.
    """
    mycar:Car = random.choice(cars)
    print(mycar)
    mycar.fuel = 10.0
    print(mycar)
    mycar.foo = 6 # adding an extra field to an instance is a bad practice
    print(mycar)
    print(mycar.foo)
    drive(mycar, 25.0)
    print(mycar)
    """ Sort the cars using a sort key lambda (aka an inline function)
    """
    # cars.sort() # can't sort cars without providing a sort key, we'll fix this with a real car class
    cars.sort(key = lambda car:car.miles, reverse = True)
    for car in cars:
        print(car)
    # carset = set(cars)  # Why can't we put the cars into a set?
    # print(carset)

if __name__ == '__main__':
    main()