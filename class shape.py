class Shape:
    def area(self):
        print("Area:")

class Circle(Shape):
    def area(self,r):
        print(3.14*r*r)

class Rectangle(Shape):
    def area(self,l,b):
        print(l*b)

class Triangle(Shape):
    def area(self,base,height):
        print(0.5*base*height)

C=Circle()
R=Rectangle()
T=Triangle()

C.area(10)
R.area(20, 5)
T.area(7, 3)
