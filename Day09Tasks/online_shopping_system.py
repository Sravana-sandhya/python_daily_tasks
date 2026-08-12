# Q9 : Online Shopping System (Multilevel Inheritance) 
# An e-commerce company organizes products using multiple levels. Create classes Product → ElectronicProduct → MobilePhone using multilevel inheritance and display product details. 
class Product:
    def display(self):
       self.name = "Smartphone"
       print("Product Name:", self.name)


class ElectronicProduct(Product):
    def display1(self):
       self.brand = "Samsung"
       print("Brand:", self.brand)


class MobilePhone(ElectronicProduct):
    def display2(self):
       self.price = 25000
       print("Price:",self.price)
m = MobilePhone()
m.display()
m.display1()
m.display2()