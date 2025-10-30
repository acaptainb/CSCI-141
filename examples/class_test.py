class Dog:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def bark(self):           # method
        print(f"{self.name} says woof!")



mydog = Dog("bobby", 23)
mydog.bark()


class Animal:
    def __init__(self, species, legs):
        self.species = species
        self.legs = legs

    def speak(self):
        return "..."  # generic animal noise, thrilling

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("dog", 4)  # call parent class
        self.name = name
        self.age = age

    def speak(self):
        return "woof"

    def __eq__(self, other):
        # equality: are two dogs the same age and name?
        if not isinstance(other, Dog):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        # less than: maybe sort dogs by age
        if not isinstance(other, Dog):
            return NotImplemented
        return self.age < other.age

    def __hash__(self):
        # allows dogs to be used in sets or dict keys
        return hash((self.name, self.age))

    def __repr__(self):
        return f"Dog({self.name!r}, {self.age})"


a = Dog("Rex", 5)
b = Dog("Rex", 5)
c = Dog("Buddy", 2)

print(a == b)  # True  -> __eq__
print(a < c)   # False -> __lt__
print({a, b, c})
# because of __hash__ and __eq__, duplicates collapse:
# {Dog('Rex', 5), Dog('Buddy', 2)}
