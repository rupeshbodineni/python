a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("biggest number is",a)
elif b>a and b>c:
    print("biggest number is",b)
else:
    print("biggest number is",c)