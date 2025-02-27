# 📍ravel & flatten function
#both convert multidimension array into 1D Array() 

#📍EXample

import numpy as np
arr=np.array([[[1,2,3,4],[4,3,56,3]],[[2,2,6,3],[6,5,3,7]]])
e=arr.flatten()
print(" before convertion Dimension :",arr.ndim)
print("one Dimension Array:",e)
print("Dimension:",e.ndim)