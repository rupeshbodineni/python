class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return f"{self.name} make a sound"
class Dog(animal):
    def speak(self):
        return f"{self.name}barks"
dog=Dog("Buddy")
print(dog.speak())