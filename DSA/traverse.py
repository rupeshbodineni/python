#Traversal
arr=[10,20,30,40,50]
for i in arr:
    print(i)

#list methods
arr=[10,20,30,40,50]
print("original list:",arr)

#append
arr=[10,20,30,40,50]
arr.append(60)
print(arr)

#insert
arr=[10,20,30,40,50]
arr.insert(5,20)
print("after insert",arr)

#remove
arr=[10,20,30,40,50]
arr.remove(20)
print("after remove:",arr)

#pop
arr=[10,20,30,40,50]
arr.pop(3)
print("after pop:",arr)

#index
arr=[10,20,30,40,50]
print("index of 30:",arr.index(30))

#count
arr=[10,20,30,40,50,50]
print("50 count:",arr.count(50))
print("10 count:",arr.count(10))

#sort
arr=[10,20,40,30,50]
arr.sort()
print("sort:",arr)

#revrse
arr=[10,20,30,40,50]
arr.reverse()
print("reverse:",arr)

#update
arr[0]=99
print("updates arr:",arr)

#clear
'''
temp=arr.copy()
temp.clear()
print("after clear:",temp)
'''
arr=[10,20,30,40,50]
arr.clear()
print("clear arr:",arr)
