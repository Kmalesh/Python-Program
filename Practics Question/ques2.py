# write a program to take 5 input from the  user and store it in a tuple.
# var1=input("Enter the first number:")
# var2=input("Enter the  second number:")
# var3=input("Enter the third number:")
# var4=input("Enter the four number :")
# var5=input("Enter the  five number:")

# b=list() #empty list 
# b.append(var1)
# b.append(var2)
# b.append(var3)
# b.append(var4)
# b.append(var5)
# tuple=(b,)#store value of list in tuple and the print tuple
# print(tuple)
# print(type(tuple))

# another way
i=1
tuple=()
for i in range(5):
    num=input("Enter the number:")
    tuple=tuple+ (num ,)# '''here comma dena jaruri hai becouse kisis
    #                    bhi integer ko ham tuple ke sath anhi add kar sakte .
    # so integer ko tuple me convert karke add karna hoga '''
    print(tuple)





