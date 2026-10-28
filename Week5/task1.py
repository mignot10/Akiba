# ==========================
# Task 1: Student Information System
# ==========================


class Student:
    # initialize the student's attributes
    def __init__(self, name, age, department):
        self.name = name 
        self.age = age
        self.department = department
    # Display the student's infomation
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("-" * 25)


student1 = Student("Abebe", 20, "Software Engineering")
student2 = Student("Hana", 21, "Computer Science")

student1.display_info()
student2.display_info()