class cars:
    def __init__(self,model,year,brand):
        self.model=model
        self.year=year
        self.brand=brand
    def display(self):
       print(f"{self.year} {self.brand} {self.model}")
car1=cars("Toyota", "Corolla", 2020)
car1.display()