'''
Unnamed data example for CSCI-141
@author RIT CS
'''
import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/car_data.csv"

def print_car(car:list)->None:
    print("A " + car[0] + " with " + \
            str(car[4]) + " miles driven that gets " + \
            str(car[3]) + " mpg, and has " + \
            str(car[2]) + " of " + str(car[1]) + " gallons")
    
def drive(car:list, distance:float)->None:
    if distance > 0:
        car[4] += distance
        car[2] -= distance/car[3]


def main():
    """ Create a list of cars from the provided datafile
    """
    cars = []
    with open(DATA_FILE) as file:
        next(file)
        for row in file:
            row = row.strip().split(",")
            new_car = [row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4])]
            cars.append(new_car)

    """ Pick a random car and do some stuff to it.
    """
    mycar = random.choice(cars)
    print_car(mycar)
    drive(mycar, 33.9)
    print_car(mycar)

if __name__ == '__main__':
    main()