class Parent:
    def __init__(self):
        print("this is parent init")

class child(Parent):
    def __init__(self):
        super().__init__()
        print("this is child init")