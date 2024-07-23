print("+ ,- ,* ,/ ,% ")
choice=(input("nter your choice:"))
num=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(choice=='+'):
    print("addition of two number is:",num+num2)

elif(choice=='-'):
    print("diffrence of two numbwr is:",num-num2)

elif(choice=='*'):
    print("multipication of two number is:",num*num2)

elif(choice=='/'):
    print("Devision of two number is:",num/num2)

elif(choice=='%'):
    print("modulo is two number is:",num%num2)

else:
    print("Ivalid Choice!!")
