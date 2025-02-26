# Create a class pets from a class Animals and further create class Dog from pets. Add a method bark to class Dog.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}."

class Pet(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    def __str__(self):
        return f"{self.name} is a {self.species}. He is a {self.breed} breed."

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", breed)

    def bark(self):
        return f"{self.name} says woof!"

a = Dog("Tashi", "German Shepherd")
print(a)
print(a.bark())