# three function used 
# 1.append() this function add new element
#2. insert() this function insert element any position
#3. remove() this function remove the elemnt from list
print("-------Registration---------\n")
print("Before the Registration unlock the page")
pin=int(input("Enter the pin no 6 digit:"))
if(pin==845423):

 list=[1,2,34,54,65,6]
 print("------MENU------")
 print("[1].Insert\n[2].Delete \n[3].Random insert\n[4].Exit")
 print("-------INSERTION AND DELETION-------")
 choice=int(input("enter the choice :"))
 if(choice==1):
  element=int(input("Enter the element:"))
  list.append(element)
  print(list)
 elif(choice== 3):
  index=int(input("enter the index no:"))
  element=int(input("Enter the element:"))
  list.insert(index,element)
  print(list)
 elif(choice== 2):
  delete=int(input("Enter the delete element:"))
  list.remove(delete)
  print(list)
 elif(choice==4):
  exit 
 else:
  print("Invalid choice!")
else:
 print("Ivalid pin! Try again")
 
 