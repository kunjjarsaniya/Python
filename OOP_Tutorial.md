
# 🐍 Python Object-Oriented Programming (OOP) Tutorial

Welcome to the beginner-friendly Python OOP tutorial! This guide introduces key object-oriented concepts with annotated code examples.

---

## 📘 Contents

- ✅ [Classes and Objects](#1-classes-and-objects)
- ✅ [Constructors and Instance Attributes](#2-constructors-and-instance-attributes)
- ✅ [Instance, Class, and Static Methods](#3-instance-class-and-static-methods)
- ✅ [Inheritance](#4-inheritance)
- ✅ [Polymorphism](#5-polymorphism)
- ✅ [Encapsulation](#6-encapsulation)
- ✅ [Abstraction](#7-abstraction)
- ✅ [Dunder (Magic) Methods](#8-dunder-magic-methods)
- ✅ [📌 Practice Exercises](#9-practice-exercises)

---

## 1. Classes and Objects

**Concept**: A class defines a blueprint. An object is an instance of that class.

```python
class Factory:
    factory_code = 12

    def greet(self):
        print("Hello! How are you?")

factory1 = Factory()
factory1.greet()
```

**🔎 Key Points**:
- `factory_code`: class attribute
- `greet()`: instance method

---

## 2. Constructors and Instance Attributes

**Concept**: The `__init__()` method initializes object attributes.

```python
class ProductFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
```

**Example**:
```python
reebok = ProductFactory("leather", 3, 2)
reebok.show_details()
```

---

## 3. Instance, Class, and Static Methods

- **Instance Method**: Uses `self` to access object-specific data.
- **Class Method**: Uses `cls` to access class-level data.
- **Static Method**: Independent of class and instance context.

```python
class Animal:
    def __init__(self, age): self.age = age
    def show_age(self): print(self.age)
    @classmethod
    def get_species(cls): print(cls.species)
    @staticmethod
    def speak(): print("Roar!")
```

---

## 4. Inheritance

**Concept**: A class can inherit properties/methods from another class.

```python
class FactoryMumbai:
    def welcome(self): print("Welcome from Mumbai factory!")

class FactoryPune(FactoryMumbai):
    pass
```

✅ *Supports multi-level inheritance with `super()` to call parent constructors.*

---

## 5. Polymorphism

**Concept**: Objects can share method names but behave differently.

```python
class Animal:
    def speak(self): print("I am an animal")

class Human(Animal):
    def speak(self): print("Hello, I am a human")
```

Used in loops to call the same method on different types of objects.

---

## 6. Encapsulation

**Concept**: Protect data by using private attributes (`__attribute`).

```python
class SecureFactory:
    __location = "Pune"
    def show_location(self):
        print(SecureFactory.__location)
```

🔒 Accessing `__location` directly will fail.

---

## 7. Abstraction

**Concept**: Abstract Base Classes enforce required methods in subclasses.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * self.radius ** 2
```

🔁 Enforces structure in derived classes.

---

## 8. Dunder (Magic) Methods

**Concept**: Special methods like `__init__`, `__str__`, `__add__`.

```python
class AnimalWithDunder:
    def __str__(self): return f"{self.name}, {self.age}"
    def __add__(self, others): return total_age
```

💡 Great for customizing how objects behave with built-in operators and functions.

---

## 9. 📌 Practice Exercises

### 🎯 Try It Yourself

- Create a `Dog` class that inherits from `Animal` and overrides `speak()`.
- Implement a `Triangle` class using the abstract `Shape` class.
- Add a `__len__()` method to return an animal's age.
- Create your own factory chain using multi-level inheritance.
- Modify `SecureFactory` to allow changing the private location safely.

---

## 📚 Further Learning

- [Python OOP Docs](https://docs.python.org/3/tutorial/classes.html)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)

---

Happy coding! 🚀
