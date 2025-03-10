
class Student:
    serial_no = 0

    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        Student.serial_no += 1

    def info(self):
        print(str(self.serial_no))
        print(self.name)
        print(str(self.ID) + "\n")

s1 = Student("Shehraz",29261)
s1.info()

s2 = Student("Ahsan",27231)
s2.info()