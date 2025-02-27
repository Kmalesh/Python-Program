import numpy as np
arr=np.array([1,2,3,4,],  dtype='S')  #capital String Required only
arr1=np.array([1,2,3,4,],  dtype='U') #unsign integer 
arr2=np.array([1,2,3,4,],  dtype='i4') #integer 4 bytes define 
arr3=np.array([1,2,3,4,],  dtype='m') #timedelta
arr4=np.array([1,2,3,4,],  dtype='f') #float
arr5=np.array([1,2,3,4,],  dtype='b') #boolean
arr6=np.array([1,2,3,4,],  dtype='c') #complex no


print(arr)
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)
print(arr6.dtype)

