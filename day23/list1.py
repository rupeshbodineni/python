nums = [10, 20, 30, 40]
fruits = ["apple", "banana", "mango"]
data = [10, "Rupesh", 95.5, True]

#accessing list elements

print(nums[1])
print(data[3])
print(fruits[2])

#indexing in list
print(nums[0])
print(fruits[2])

#negative indexing
print(fruits[-1])
print(fruits[0])
print(data[-3])

#slicing in list
a = [10, 20, 30, 40, 50]
print(a[1:4])  
print(a[0:3])
print(a[1:5])
print(a[1:7])
print(a[::-1])


#removing
a.remove(30)
print(a)
a.insert(2,30)
print(a)

x=a.pop()
print(x)

a.remove(10)
print(a)

