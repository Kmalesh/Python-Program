# mov1=input("Enter the first movie name:")
# mov2=input("Enter the second  movie name:")
# mov3=input("Enter the third movie name:")
# list=[]
# list.append(mov1)
# list.append(mov2)
# list.append(mov3)
# print(list)

list=[1,"recer",1]
copy1=list.copy()
copy1.reverse()
if(copy1==list):
    print("yes")
else:
    print("NO")    