arr=[10,20,30,40,50]
key=30
for i in range (len(arr)):
    if arr[i]==key:
        print("found index",i)
        break

#2d array
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 
for i in range(len(matrix)):
    row_sum=0
    for j in range(len(matrix[i])):
        row_sum +=matrix[i][j]
print("Row",i+1,"sum=",row_sum)