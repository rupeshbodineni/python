def outer():
    def inner():
        print("inner function ")
    return inner

result=outer()
print(result)
