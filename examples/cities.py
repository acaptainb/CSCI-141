"""
CSCI-141 Computer Science 1 Recitation Code
10-Classes
Dataclasses: Cities

A program that demonstrates the use of a dataclass structure via the use of the
class keyword and the dataclass annotation.

This program reads a collection of cities from a file, cities.txt, into a
list of City objects that are then iterated over in order to draw the
lines and labels between each city and back to the first.
"""

from dataclasses import dataclass
import turtle

@dataclass
class City:
    """
    A dataclass representing a city.
    """
    name: str      # the name of the city
    x: int         # the x coordinate of the city
    y: int         # the y coordinate of the city
    def __init__(self, name, x, y):
        self.name = name
        self.x=x
        self.y=y

def read_cities(filename):
    """
    Read the cities from the filename into a list of City objects.  We expect
    each line of the file to be in the format:

        city_name, x_coordinate, y_coordinate

    :param filename: the name of the file
    :return: the list of City objects
    """
    cities = []
    with open(filename) as f:
        for line in f:
            fields = line.split(',')     # fields = ['city_name', 'x_coord', 'y_coord']

            # create and append a new City object
            cities.append(City(fields[0], int(fields[1]), int(fields[2])))

    return cities

def draw_map(cities):
    """
    Using turtle draw a map of the cities with lines between each city
    and a label.

    :param cities: list of City objects
    """
    # go to coordinate of the last city
    turtle.up()
    turtle.goto(cities[-1].x, cities[-1].y)
    turtle.down()

    # loop over the cities
    for city in cities:
        # draw line to this city and write the name
        turtle.goto(city.x, city.y)
        turtle.write(city.name, False, align="center", font=('Arial', 16, 'bold'))

    turtle.hideturtle()

def main():
    # read the City objects from the file into the list, cities
    cities = read_cities(r'C:\Users\acapt\OneDrive\Desktop\CSCI 141\examples\cities.txt')

    # print each City object in cities to standard output
    for city in cities:
        print(city)

    # draw the map of cities
    draw_map(cities)

    turtle.done()

if __name__ == '__main__':
    main()

"""
$ python3 cities.py
City(name='A', x=0, y=0)
City(name='B', x=100, y=0)
City(name='C', x=50, y=25)
"""