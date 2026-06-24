class vehicle:
    def __init__(self,car):
        self.car=car
        

class car(vehicle):
    def ride(self):
        return f"{self.car} car is driving"
c1=car("bmw")
print(c1.ride())