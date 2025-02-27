import numpy as obj
arr=obj.array([12,2,3,4,5,3,2,5,46,4,])

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            arr[j]=-1
            break
for i in range(len(arr)):
    if arr[j]<0:
        print(arr[j])