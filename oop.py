# object_oriented_programming.py
# ---------------------------------
# Beginner-friendly Python OOP tutorial
# Covers: Classes, Objects, Constructors, Inheritance, Polymorphism, Encapsulation, Abstraction, Dunder Methods
# Each section includes explanations and examples

from abc import ABC, abstractmethod

# ==========================================
# 1. Basic Class and Object Creation
# ==========================================

class Factory:
    # Class attribute shared among all instances
    factory_code = 12

    def greet(self):  # Instance method
        print("Hello! How are you?")

# Creating objects (instances) of Factory
factory1 = Factory()
factory2 = Factory()

# Accessing method
factory1.greet()

# ------------------------------------------
# Try This:
# - Print factory1.factory_code
# - Add another method like `shutdown()` to Factory class

# ==========================================
# 2. Constructor and Instance Attributes
# ==========================================

class ProductFactory:
    def __init__(self, material, zips, pockets):
        # Instance attributes (unique to each object)
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show_details(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

# Creating instances with different data
reebok = ProductFactory("leather", 3, 2)
campus = ProductFactory("nylon", 3, 3)

reebok.show_details()
campus.show_details()

# ==========================================
# 3. Instance, Class, and Static Methods
# ==========================================

class Animal:
    species = "Lion"  # Class attribute

    def __init__(self, age):
        self.age = age  # Instance attribute

    def show_age(self):
        print(f"The animal is {self.age} years old.")

    @classmethod
    def get_species(cls):
        print(f"Species: {cls.species}")  # Access class-level data

    @staticmethod
    def speak():
        print("Roar!")  # No self/cls — just performs a task

lion = Animal(5)
lion.show_age()
Animal.get_species()
Animal.speak()

# ------------------------------------------
# Try This:
# - Create another animal (e.g., dog) and call all three methods

# ==========================================
# 4. Inheritance (Single & Multi-Level)
# ==========================================

# Single Inheritance
class FactoryMumbai:
    location = "Mumbai"

    def welcome(self):
        print("Welcome from Mumbai factory!")

class FactoryPune(FactoryMumbai):
    pass  # Inherits everything from FactoryMumbai

pune_factory = FactoryPune()
pune_factory.welcome()

# Multi-level Inheritance
class BaseFactory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(BaseFactory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

# ------------------------------------------
# Try This:
# - Create a PuneFactory object and print its attributes

# ==========================================
# 5. Polymorphism
# ==========================================

class Animal:
    def speak(self):
        print("I am an animal.")

class Human(Animal):
    def speak(self):
        print("Hello, I am a human.")

# Polymorphism in action
for creature in [Animal(), Human()]:
    creature.speak()

# ------------------------------------------
# Try This:
# - Add another subclass (e.g., Dog) and override speak()

# ==========================================
# 6. Encapsulation (Data Hiding)
# ==========================================

class SecureFactory:
    __location = "Pune"  # Private attribute (name mangled)

    def show_location(self):
        print(f"Factory location is {SecureFactory.__location}")

secure = SecureFactory()
secure.show_location()

# ------------------------------------------
# Try This:
# - Try accessing `secure.__location` directly and see what happens

# ==========================================
# 7. Abstraction using ABC (Abstract Base Class)
# ==========================================

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

square = Square(4)
circle = Circle(5)

print("Square area:", square.area())
print("Circle perimeter:", circle.perimeter())

# ------------------------------------------
# Try This:
# - Add a Triangle class and implement area/perimeter

# ==========================================
# 8. Dunder (Magic) Methods
# ==========================================

class AnimalWithDunder:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal name: {self.name}, Age: {self.age}"

    def __add__(self, others):
        total_age = self.age + sum(obj.age for obj in others)
        return f"Total combined age: {total_age}"

a1 = AnimalWithDunder("Lion", 12)
a2 = AnimalWithDunder("Dolphin", 14)
a3 = AnimalWithDunder("Tiger", 34)

print(a1)  # Calls __str__
print(a1 + (a2, a3))  # Calls __add__

# ------------------------------------------
# Try This:
# - Add a __len__ method to return animal age
# - Override __eq__ to compare animals by age
