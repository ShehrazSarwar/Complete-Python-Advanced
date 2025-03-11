import time
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):  #this class child one must implement all abstract methods
    def start(self):
        print("Start..")

    def stop(self):
        print("Stopped...")

car1 = Car()
car1.start()
time.sleep(2)
car1.stop()