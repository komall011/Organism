'''You are tasked with creating a simple program to model biological organisms. For this, you need to define a class called Organism with appropriate attributes and methods.

Create a class called Organism with the following attributes:

name (a string): representing the name of the organism.
species (a string): representing the species of the organism.
age (an integer): representing the age of the organism in months.
is_alive (a boolean): representing whether the organism is alive or not. By default, set it to True.
Define a constructor (an _init_ method) for the Organism class that initializes the name, species, and age attributes.

Implement a method called grow that takes an integer argument months and increases the age of the organism by that number of months. Also, check if the age exceeds 120 months (10 years) and if so, set is_alive to False.

Implement a method called is_dead that returns True if the organism is not alive (i.e., if is_alive is False) and False otherwise.

Make the name and species attributes private so that they can only be accessed within the class.

Provide a way to access the name and species attributes using getter methods (e.g., get_name() and get_species()).

Create an instance of the Organism class with the name "Bob," species "Human," and an initial age of 30 months. Simulate Bob's growth by making him age 60 more months, and then check if he is alive.'''

class Organism: # define organism class (need to pass self arguemts for all functions/ methods)
    def __init__(self, name:str, species:str, age:int) -> None: # define constructor with attributes (with data type) and set initial values with parameters for name, species, age
        self.__name = name # private, can only retrieved with getName()
        self.__species = species # private, can only be retrieved with getSpecies()
        self.age = age # in months
        self.is_alive = True # default = true

    def grow(self, months:int) -> int: # grow method, months param is an int and return must be int
        if self.age <= 120: # if less than or equal 120, then add to age
            self.age += months # add months to age
        else: # 120 months = 10 years
            self.is_alive = False # is dead, change is_alive to false
        return self.age
    
    def isDead(self) -> bool: # define is dead method would return either True or False
        return not self.is_alive # return opposite boolean of is_alive
    
    def getName(self) -> str: # getter for name bc private, return string
        return self.__name
    
    def getSpecies(self) -> str: # getter for species bc private, return string
        return self.__species
    
bob = Organism("Bob", "Human", 30) # create an organism objects: Bob, Human, 30 months old

print(bob.age) # initial age = 30 months

bob.grow(60) # age = 30 + 60 = 90 months and should be alive

# checks
print(bob.getName()) # Bob
print(bob.getSpecies()) # Human
print(bob.age) # 90 months
print(bob.is_alive) # True
print(bob.isDead()) # False

print(bob.grow(40))
print(bob.age)
print(bob.isDead())

print(bob.grow(40))
print(bob.age)
print(bob.isDead())

alice = Organism("Alice","Human",100)
print(alice.age)

if bob.age > alice.age:
    print("Bob is older")
else:
    print("Alice is older")