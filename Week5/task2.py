# ==========================
# Task 2: Rectangle Calculator
# ==========================


class Rectangle:
     # Initialize length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate the area
    def area(self):
        return self.width * self.length
    
    # Calculate the perimeter
    def perimeter(self):
        return  2 * (self.length + self.width)

# Create two rectangle objects
r1 = Rectangle(2,3)
r2 = Rectangle(10, 5)

# Display the area and perimeter of the first rectangle
print("Rectangle 1:")
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print('=' * 20)

print("Rectangle 2:")
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())
