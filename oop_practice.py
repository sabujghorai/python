# Define a Circle class to create a circle  without radiu using the constructor
# Define Area() method and Perimeter() method 

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return 3.14*self.radius**2
    
    def Perimeter(self):
        return 2*3.14*self.radius


a = int(input("Enter the radius :"))
c2 = Circle(a)
print(c2.Area())
print(c2.Perimeter())
