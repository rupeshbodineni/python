# def sub(a,b):
#     print(a-b)

# sub(a=10,b=20)
# sub(b=200,a=100)
# sub(10,20,30)

# def add(a, *b):
#     print(a)
#     print(b)
# add(10,20)
# add(10,20,30)
# add(10,20,30,40)

def display(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
print(10,20,30,"name":"rahul","")