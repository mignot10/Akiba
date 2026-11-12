from abc import ABC, abstractmethod
import math


# Abstract parent class
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


# Rectangle child class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Circle child class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Display calculated areas
print("Rectangle area:", rectangle.calculate_area())
print("Circle area:", circle.calculate_area())




#Answer
# 1. What is polymorphism?
# Polymorphism means "many forms." It allows different classes
# to have methods with the same name but different implementations.
# Example: Dog, Cat, and Cow all have make_sound(), but produce
# different sounds.


# 2. What is abstraction?
# Abstraction is the process of hiding unnecessary implementation
# details and exposing only the essential functionality.
# It focuses on what an object does rather than how it does it.


# 3. What is an abstract class?
# An abstract class is a class that cannot be instantiated directly.
# It is used as a blueprint for child classes.
# In Python, we can create abstract classes using ABC and
# define abstract methods using @abstractmethod.


# 4. What happens if a child class does not implement an inherited
# abstract method?
# The child class also remains abstract and cannot be instantiated.
# Python raises a TypeError if we try to create an object from it.


# 5. What is the difference between abstraction and encapsulation?
# Abstraction hides implementation details and exposes essential
# functionality. It focuses on WHAT an object does.
#
# Encapsulation bundles data and methods inside a class and
# controls access to the object's internal data.
# It focuses on protecting and managing HOW data is accessed
<<<<<<< HEAD
# and modified.
=======
# and modified.
>>>>>>> e285649 (Add Library Management System mini project)
