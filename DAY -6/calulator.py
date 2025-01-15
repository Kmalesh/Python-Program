print("****************CALCULATOR****************\n")

print("[1].addition\n[2].subtrction\n[3].Multipication\n[4].Devision\n[5].Reminder_find\n")
i=1
while(i<10):

    ch=int(input("Enter your choice:"))
    num=int(input("Enter the first number:"))
    num2=int(input("Enter the second number :"))

    if ch==1:

        print("addition of two number:",num+num2)

    elif ch==2:
        print("Subtraction of two number is:",num-num2)

    elif ch==3:
        print("multipication of two number:",num*num2)

    elif ch==4:
        print("Devision of two number:",num/num2)

    elif ch==4:
        print("Reminder of two number is:",num%num2)

    else:
        print("Invalid! choice\n")
