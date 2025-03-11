# Another way to achieve Polymorphism

class Animal:
    isAlive = True

class Dog(Animal):
    @staticmethod
    def speak():
        print("WOOF!")

class Cat(Animal):
    @staticmethod
    def speak():
        print("MEOW!")

class Car:    #Duck Typing Example Car
    @staticmethod
    def speak():
        print("HONK!")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()