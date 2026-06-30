def smart_division(func):
    def inner(a, b):
        if b == 0:
            print("Division by zero is not allowed")
        else:
            print("Division is possible")
            func(a, b)
    return inner


@smart_division
def add(a, b):
    print(a / b)
    print("Hello World")


add(10, 2)

