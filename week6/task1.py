class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id= student_id
        self.department = department
    def display_info(self):
        print('=' * 20)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print('=' * 20)

    def introduce(self):
        print(f"Hello, my name is {self.name} and I study {self.department}.")


student1 = Student("Egelit Egele", "ST-1001", "CS")
student1.display_info()
student1.introduce()