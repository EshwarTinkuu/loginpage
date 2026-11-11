
class Student:

    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Instance method
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)
        print("-------------------")



student1 = Student("Eshwar", 23, "Python")
student2 = Student("Rahul", 22, "Java")
student3 = Student("Arjun", 21, "MERN Stack")



student1.display()
student2.display()
student3.display()
