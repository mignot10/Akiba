# ==========================
# Task 3: Student Score Management
# ==========================


class Student:
    # Class attribute (shared by all students)
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        # Instance attributes (belong to each student)
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print("School:", self.school_name)
        print("Name:", self.name)
        print("Score:", self.score)
        print("Department:", self.department)
        print("-" * 30)


student1 = Student("Abel", 85, "Software Engineering")
student2 = Student("Sara", 92, "Computer Science")
student3 = Student("Dawit", 78, "Information Systems")

# Display the original information
print("Original student information:")
student1.display()
student2.display()
student3.display()

# Update one student's score
student1.score = 95

# Display the updated information
print("After updating Abel's score:")
student1.display()

# Demonstrate independent scores
print("Other students' scores:")
print(student2.name, ":", student2.score)
print(student3.name, ":", student3.score)
