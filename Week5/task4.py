# ==========================
# Task 4: Product Information System
# ==========================

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price} Birr, Quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity


# Create three product objects
product1 = Product("Laptop", 45000, 2)
product2 = Product("Mouse", 800, 5)
product3 = Product("Keyboard", 1500, 3)

# Print each object directly
print(product1)
print("Total value:", product1.total_value(), "Birr")
print()

print(product2)
print("Total value:", product2.total_value(), "Birr")
print()

print(product3)
print("Total value:", product3.total_value(), "Birr")
