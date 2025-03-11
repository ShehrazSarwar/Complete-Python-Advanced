# Class variables (use it like static variable in Java)

class Student:
    serial_no = 0  # Class variables
    # College name is always same for each student so it's better to use College name as a class variable
    college_name = "IQRA"

    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        # We can increment the class variable to calculate the no of students
        Student.serial_no += 1  #Always Access them using Class Name

    def info(self):
        print(str(Student.serial_no))  #good practice to use class name with class variables
        print(self.name)
        print(str(self.ID))

s1 = Student("Shehraz",29261)
s1.info()
print(Student.college_name, end= "\n\n")  #Can also access directly from here too!

s2 = Student("Ahsan",27231)
s2.info()
print(Student.college_name)