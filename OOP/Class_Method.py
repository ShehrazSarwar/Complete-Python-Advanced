# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name}, {self.gpa}"

    @classmethod
    def total_students(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"


Student1 = Student("Shehraz",3.91)
Student2 = Student("Umer",3.1)
Student3 = Student("Ali",3.3)

print(Student.total_students())
print((Student.get_average_gpa()))