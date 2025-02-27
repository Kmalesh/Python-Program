# split function:- breakdown into sub array according to your requred


import numpy as np
arr=np.array([[[1,2,3,4],[4,3,56,3]],[[2,2,6,3],[6,5,3,7]]])
arr1=np.array_split(arr,2)
print(arr1)