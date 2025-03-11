# Super()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, id_no):
        super().__init__(name,age)  #using person class Constructor super class
        self.id_no = id_no

    def emp_id(self):
        print(f"Employee ID: {self.id_no}")

    def emp_info(self):
        print("Simple Employee")
        super().person_info()  #using super class function
        self.emp_id()


employee = Employee("Jake",25,2313)
employee.emp_info()
