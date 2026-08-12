# Q5 : Vehicle Management System (Inheritance) 
#A transport company manages different vehicles. Create a base class Vehicle with attributes like brand and speed. Create derived classes Car and Bike that inherit from Vehicle and display their details.
class Vehicle:
    def __init__(self,brand,speed):
      self.brand = brand
      self.speed = speed
class Car(Vehicle):
    def display(self):
       print("Car Details")
       print("Brand:", self.brand)
       print("Speed:", self.speed)
class Bike(Vehicle):
   def display(self):
        print("Bike Details")
        print("Brand:", self.brand)
        print("Speed:", self.speed)
car = Car("Toyota", 180)
bike = Bike("Duke",120)
car.display()
print()
bike.display()


  