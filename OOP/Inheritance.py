# Simple Single Level inheritance:
# One parent class Animal(Super) and two child classes(Derived) Dog and Cat

class Animal:
    def __init__(self, name, color):  #always pass self in python
        self.name = name
        self.color = color

    def sleep(self):
        print(f"{self.name} is asleep")

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} Barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meow")


dog = Dog("Bob","Brown")
dog.speak()
dog.sleep()
dog.eat()
print()
cat = Cat("Tom","Blue")
cat.speak()
cat.sleep()
cat.eat()