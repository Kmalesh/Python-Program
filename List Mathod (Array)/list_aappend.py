# append function means add karna kisi bhi number ka.
# List muetable hota hai jisme ham changes kar sakte hai.

list=[1,3,4,7,1,9,22,16]
list.append(50)#add integer
list.append(51)# add number
list.append(55)
print("Without sorting :",list)

list.sort()
print("After sorting:",list)# only ascending order 

#for Descending order
list.sort(reverse=True)
print("Descending Order:",list)

