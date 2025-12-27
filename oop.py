class Car: # first letter must be capital letter 'c'ar
    car_name = "Mercedese Benz"
    model_no = 23
    colour = "Blue"

s1 = Car() # creating aa object
print(s1.car_name)
print(s1.model_no)
print(s1.colour)


# __init__ function --> also call constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("mercedese","53")
print(my_car.brand)
print(my_car.model)
