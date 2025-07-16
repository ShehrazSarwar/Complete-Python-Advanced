#Python OOP ---> Classes, Objects, Attributes & Methods

class Student:
    #college = "Iqra"   #Attributes

    def __init__(self, name, age, college = 'Iqra'):  #Constructor (Parameterized)
        self.name = name
        self.age = age
        self.college = college
        self.courses = []

    def add_course(self, course):   #Method
        self.courses.append(course)

    def display_info(self):   #Method
        print("Name: " + self.name + "\nCollege: "+ self.college + "\nAge: " + str(self.age) +
              "\nCourses: " + ', '.join(self.courses))


s1 = Student("Shehraz", 20)
s1.add_course("Data Science")
s1.add_course("Comp Science")
s1.display_info()

