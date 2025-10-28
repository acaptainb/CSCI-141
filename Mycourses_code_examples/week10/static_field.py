fruit_names = ["apple", "pear", "orange", "banana"]

class Fruit:
    ID_SEQ = 1 # this attribute is part of the CLASS so it's the only one!
    __slots__ = ['name', 'id']
    name:str
    id:int

    def __init__(self, name:str):
        self.name = name
        self.id = Fruit.ID_SEQ
        Fruit.ID_SEQ += 1

    def __repr__(self)->str:
        return "Fruit: " + str(self.id) + " : " + self.name
    
fruits = []
for name in fruit_names:
    new_fruit = Fruit(name)
    fruits.append(new_fruit)

for fruit in fruits:
    print(fruit)