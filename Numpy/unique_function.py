#unique function :- it give unique value 
import numpy as obj
arr=obj.array([12,2,3,4,5,3,2,5,46,4,])
arr1=obj.unique(arr,return_counts=True)#return_counts=True, (always gives how many time repeate the value)
arr2=obj.unique(arr,return_index=True)#return index value
print(arr)
print("unique value is :",arr1)
print("unique value is :",arr2)
