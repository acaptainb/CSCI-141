"""
CSCI-141 Computer Science 1 Recitation Code
10-Classes
Pair Exercise

This pair exercise has students explore the similarities and differences
between a dataclass used strictly as a structure, versus a full-blown
class.

The dataclass, Point, is a frozen 2-D point.
The class, Polygon, is used to represent a polygon as a collection of Point objects.

1. The program first reads the polygon from an input file.  See bird.txt and fish.txt.
2. It computes the perimeter and area for bird.txt and then plots it.
3. It computes the perimeter and area for fish.txt and then plots it.
4. Finally, it demonstrates the hashablity and equality of Polygon objects.

Student exercises:
1. Implement __str__
2. Implement compute_perimeter
3. Implement __eq__
"""

import math
import turtle
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    """
    A dataclass representing a 2-D point.
    """
    label: str    # the unique label string for the point
    x: int        # x coord
    y: int        # y coord

class Polygon:
    """
    A class representing a polygon as a collection of Point objects.
    """
    __slots__ = ('name', 'points')
    name: str                       # the name of the polygon
    points: tuple[Point, ...]       # a collection of immutable points

    def __init__(self, filename: str):
        """
        Reads the input file and creates a new Polygon object.  Refer to bird.txt and
        fish.txt for the format.
        :param filename: the polygon file
        """
        # file handling
        with open(filename, 'r') as f:
            self.name = f.readline().strip()
            points = []
            for line in f.readlines():
                fields = line.split(',')
                point = Point(fields[0], int(fields[1]), int(fields[2]))
                points.append(point)
            self.points = tuple(points)   # convert list to tuple
        # turtle initialization
        turtle.Screen().setup(600, 600)
        turtle.setworldcoordinates(0, 0, 9, 9)

    def compute_perimeter(self) -> float:
        """
        Computes the total perimeter of the polygon by looping over the vertices
        and computing the distance of each line segment.
        :return float: the perimeter of the polygon
        """
        # TODO: Step 2
        perimenter =0
        for i in range(len(self.points) -1):
            p1=self.points[i]
            p2=self.points[i+1]
            perimenter+= math.sqrt(math.pow(p1.x -p1.y, 2)+
                                    math.pow(p2.x -p2.y,2 ))
        return perimenter

    def compute_area(self) -> float:
        """
        Computes the area of the polygon by looping over the vertices and applying the
        shoelace formula: Area = 1/2 * |(x1y2 + x2y3 + ... + xny1) - (y1x2 + y2x3 + ... + ynx1)|
        :return float: the area of the polygon
        """
        xy_sum = 0
        for xi in range(len(self.points)-1):
            xy_sum += self.points[xi].x * self.points[xi+1].y
        xy_sum += self.points[-1].x * self.points[0].y
        yx_sum = 0
        for yi in range(len(self.points)-1):
            yx_sum += self.points[yi].y * self.points[yi+1].x
        yx_sum += self.points[-1].y * self.points[0].x
        return .5 * math.fabs(xy_sum - yx_sum)

    def plot(self) -> None:
        """ Plot the polygon using turtle."""
        turtle.clearscreen()
        turtle.write(self.name, False, align="left", font=('Arial', 24, 'bold'))
        turtle.up()
        turtle.hideturtle()
        for point in self.points:
            turtle.goto(point.x, point.y)
            turtle.down()
            turtle.dot(10)
            turtle.write(point.label, False, align="left", font=('Arial', 24, 'bold'))
        turtle.goto(self.points[0].x, self.points[0].y)

    def __str__(self) -> str:
        """
        Returns a string representation of the polygon in the format:
        Polygon_Name
        Vertex1_Name (x1,y1)
        ...
        :return: the string representation of the polygon
        """
        # TODO: Step 1
        print_str = self.name +"\n"
        for vertex in self.points:
            print_str+=f"{vertex.label} ({vertex.x} {vertex.y}) \n "
        return print_str

    def __eq__(self, other) -> bool:
        """
        Two polygons are equal if they have the same name and same set of points.
        :return bool: equal or not
        """
        # TODO: Step 3
        return self.name ==other.name and self.points == other.points

    def __hash__(self) -> int:
        """
        The hash code of a Polygon is the sum of the name's hash and the points hash.
        :return: int: hash code
        """
        return hash(self.name) + hash(self.points)


def main():
    """The main method"""
    # fish is first
    fish = Polygon(r'C:\Users\acapt\OneDrive\Desktop\CSCI 141\examples\fixh.txt')
    print(fish, end='')
    print('Fish Perimeter:', fish.compute_perimeter())
    print('Fish Area:', fish.compute_area())
    fish.plot()

    input('Hit enter to continue...')

    # bird is second
    bird = Polygon(r'C:\Users\acapt\OneDrive\Desktop\CSCI 141\examples\bird.txt')
    print(bird, end='')
    print('Bird Perimeter:', bird.compute_perimeter())
    print('Bird Area:', bird.compute_area())
    bird.plot()

    # create a duplicate fish
    fish2 = Polygon('fish.txt')
    # adding these to the set should result in one fish and one bird only
    animals = {fish, bird, fish2, bird}
    print("Unique Animals:")
    for animal in animals:
        print(animal.name)
    # equality checks
    print('fish == fish2?', fish == fish2)
    print('bird == fish?', bird == fish)

    turtle.mainloop()

if __name__ == '__main__':
    main()

