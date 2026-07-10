class cars:
    def __init__(self,brand,price,manufacturedyear):
        self.brand=brand
        self.price=price
        self.manufacturedyear=manufacturedyear

c1=cars("bmw",500000,2000)
print(c1.manufacturedyear)
print(c1.brand)
print(c1.price)