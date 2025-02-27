#10,20,30,40,
#70,80,90,100
#44,55,66,77
#102,103,104,105

import numpy as np 

               # for Access 0-0  #for access 0-1    # yaha se 1-0     #For Access 1-1
arr=np.array([[[10,20,30,40,50],[60,70,80,90,100]],[[44,55,66,77,88],[11,102,103,104,105]]])
# print(arr.shape)

print(arr[0,0,0:4])
print(arr[0,1,1:5])
print(arr[1,0,0:4])
print(arr[1,1,1:5])