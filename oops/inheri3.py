class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class developer(employee):
    def __init__(self, name, age,city):
        super().__init__(name, age)
        self.city=city

    def sound(self):
        print(f"{self.name} is working on {self.city}")

d1=developer("rupesh",21,"banglore")
print(d1.name)
print(d1.age)
print(d1.city)
d1.sound()