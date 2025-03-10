#Python OOP ---> Classes, Objects, Attributes & Methods
from typing import override

class Student:
    college = "Iqra"   #Attributes
    courses = []

    def __init__(self, name, age):  #Constructor (Parameterized)
        self.name = name
        self.age = age

    def add_course(self, course):   #Method
        self.courses.append(course)

    def display_info(self):   #Method
        print("Name: " + self.name + "\nCollege: "+ self.college + "\nAge: " + str(self.age) +
              "\nCourses: " + str(*self.courses))


s1 = Student("Shehraz", 20)
s1.add_course("Data Science")
s1.display_info()

