'''
Class example for CSCI-141
@author RIT CS
'''
import os
import random

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/car_data.csv"

class Car:
    '''
    Represents a car and its ability to drive and consume fuel
    '''
    __slots__ = ('model','tanksize','fuel','mpg','miles')
    model: str
    tanksize: float
    fuel: float
    mpg: float
    miles: float
    
    def __init__(self, model:str, tanksize:float, mpg:float)->None:
        '''
        Constructor
        :param model: Car model
        :param tanksize: Size of the gas tank
        :param mpg: Fuel mileage of the car
        '''
        self.model = model
        self.tanksize = tanksize
        self.mpg = mpg
        self.fuel = tanksize
        self.miles = 0

    def drive(self,distance:float)->None:
        '''
        Drive the car the given distance, do not drive backward!
        :param distance: distance to drive
        '''
        if distance > 0:
            self.miles += distance
            self.fuel -= distance/self.mpg

    def set_fuel(self,amount:float)->None:
        '''
        Put fuel in the car, but not too much!
        :param amount: Amount of fuel to add
        '''
        if self.fuel + amount <= self.tanksize:
            self.fuel = amount
        else:
            self.fuel = self.tanksize

    def __str__(self)->str:
        '''
        String representation of the car
        :return: String representation
        '''
        return "A " + self.model + " with " + \
            str(self.miles) + " miles driven that gets " + \
            str(self.mpg) + " mpg, and has " + \
            str(self.fuel) + " of " + str(self.tanksize) + " gallons"
    
    def __repr__(self)->str:
        return str(self)

    def __eq__(self, other)->bool:
        '''
        Equality test for cars, need to have the same model name and tank size
        :param other: Car to compare to itself
        :return: equality
        '''
        return self.model == other.model and self.tanksize == other.tanksize
    
    def __hash__(self)->int:
        '''
        Hash for cars, uses same info as eq
        :param other: Car to compare to itself
        :return: hash code
        '''
        return hash(self.model) + hash(self.tanksize)
    
    def __lt__(self, other)->bool:
        '''
        Less than for cars compares models
        :param other: Car to compare to itself
        :return: boolean
        '''
        return self.model < other.model

def main():

    """ Create a list of cars from the provided datafile
    """
    cars = []
    with open(DATA_FILE) as file:
        next(file)
        for row in file:
            row = row.strip().split(",")
            new_car = Car(row[0],float(row[1]),float(row[3]))
            cars.append(new_car)
    
    cars = cars[:10]

    # for car in cars:
    #     print(car)

    mycar = random.choice(cars)
    print(mycar)
    mycar.drive(100)
    print(mycar)
    # mycar.foo = 10 slots prevents us from adding instance fields
    samecar = mycar
    print("mycar == samecar:", samecar == mycar)
    print("mycar is samecar:", samecar is mycar)
    anothercar = Car(mycar.model, mycar.tanksize, mycar.mpg)
    print("mycar == anothercar:", mycar == anothercar)
    print("mycar is anothercar:", mycar is anothercar)
    print()

    print("Car list - sorted (naturally by model name)")
    cars.sort()
    for car in cars:
        print(car)
    print()

    cars.sort(key = lambda car:car.mpg, reverse = True )
    print("Car list - sorted (reverse by mpg)")
    for car in cars:
        print(car)
    print()

    print("Put the cars into a dictionary")
    cardict = {}
    for car in cars:
        cardict[car.model] = car
    print(cardict)

if __name__ == '__main__':
    main()