class Vehicle:
    brand = "Royal Enfield"
    model = "Classic-350"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    color = "Black"
    model = "HyRider"


class Bike(Car):
    color = "Brown"
    engine = "350cc"


v = Vehicle()
c = Car()
b= Bike()

v.display()
c.display()
b.display()

print("Car color:", c.color)
print("Bike color:", b.color)
print("Bike engine:", b.engine)

    
    
            
    