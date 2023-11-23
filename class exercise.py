from abc import ABC, abstractmethod

# encapsulation (vehicle class with private atributes)
class Vehicle:
    def __init__(self, make, model):
        self._make = make  
        self._model = model  
        self.engine_start = False

    @abstractmethod
    def start_engine(ABC):
        pass #abstraction to let subclassses decide

    def display_info(self):
        print(f"{self._make} {self._model} {self.engine_start}")

# inheritence car inherits vehicle properties
class Car(Vehicle):
    def start_engine(ABC):
        print("Car engine started")  #polymorphism: overriding the start engine class
        ABC.engine_start = True


class Motorcycle(Vehicle):
    def start_engine(ABC):
        print("Motorcycle engine started")
        ABC.engine_start = True

# Polymorphism: Function that takes any Vehicle object and calls start_engine
def start_any_engine(vehicle):
    vehicle.start_engine()


car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Harley-Davidson", "Sportster")


start_any_engine(car)  

car.display_info() 
motorcycle.display_info()  
