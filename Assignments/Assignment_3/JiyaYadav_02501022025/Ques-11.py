#Create a student class with name and marks 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
# Create an instance of the Student class
student1 = Student("Jiya Yadav", 85)
# Display student details
student1.display_details()
        