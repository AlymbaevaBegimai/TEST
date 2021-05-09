
class Car:
    maker = ""
    

    def __init__(self, model, maker):
        self.model = model
        self.maker = maker
    
    

class Honda(Car):
    weight = 1000

    def add(self, kg):
        self.weight += kg

car_1 = Car(model="Kalina", maker="Lada") 
print(car_1.maker)

car_2 = Honda(model="1234", maker='Kris')
car_2.add(100)
print(car_2.weight)