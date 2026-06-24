class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):          # Diamond problem
    def __init__(self):
        print("D init")
        super().__init__()


d = D()
# Output order: D → B → C → A