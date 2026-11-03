# Parent / Base Class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Parent display method
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")


# Child Class 1: Inherits from Employee
class Manager(Employee):

    def __init__(self, name, salary, department):
        # super().__init__() passes 'name' and 'salary' to the parent Employee constructor
        super().__init__(name, salary)
        self.department = department  # Child-specific attribute

    # Overrides display_info() to customize output for a Manager
    def display_info(self):
        # Calls the parent class method to print Name and Salary (reusing code)
        super().display_info()
        # Adds the Manager information
        print(f"Department: {self.department}")


# Child Class 2: Inherits from Employee
class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        # Uses super() to let the parent handle 'name' and 'salary'
        super().__init__(name, salary)
        self.programming_language = programming_language  # Child-specific attribute

    # Overrides display_info() to customize output for a Developer
    def display_info(self):
        # Reuses parent logic for Name and Salary
        super().display_info()
        # Adds the Developer information
        print(f"Programming Language: {self.programming_language}")



emp = Employee("Abebe Bikila", 50000)
mgr = Manager("Sara Kebede", 85000, "Engineering")
dev = Developer("saba Bekele", 70000, "Python")

# Call display_info() on each object to demonstrate inheritance & overriding
print("--- Base Employee Info ---")
emp.display_info()

print("\n--- Manager Info ---")
mgr.display_info()

print("\n--- Developer Info ---")
dev.display_info()