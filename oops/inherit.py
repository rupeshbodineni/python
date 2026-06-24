class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return f"{self.name} make a sound"
class Dog(animal):
    def speak(self):
        return f"{self.name}barks"
    
class Tiger(animal):
    def speak(self):
        return f"{self.name} roars"
dog=Dog("Buddy")
print(dog.speak())
Tiger=Tiger("tiger")
print(Tiger.speak())