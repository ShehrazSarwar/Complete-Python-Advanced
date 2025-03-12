# More Advanced OOP Concept Property Decorator
# @property = Decorator used to define a method as a property
# It can be accessed like an attribute
# Gives you setter, getter and deleter method
# Useful when doing Encapsulation

class Rectangle:
    def __init__(self, width, height):
        # _var  --> protected  (protected also needs getters and setters)
        # __var --> private
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, new_value):
        if new_value > 0:
            self.__width = new_value
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_value):
        if new_value > 0:
            self.__height = new_value
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self.__width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self.__height
        print("Height has been deleted")

rectangle = Rectangle(3,4)
print(rectangle.width)  #no need to call a method (that's how @property helps)
print(rectangle.height)

rectangle.width = 0    # ---> (this need a setter method)
rectangle.width = 6
rectangle.height = 5

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height