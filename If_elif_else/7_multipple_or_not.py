num=int(input("Enter the number:"))

num1=("not 7 multiply","yes 7 multiply" )[num%7==0]
print(num1)

# two ways
num=int(input("Enter the number:"))
if(num%7==0):
    print("multiple is 7")
else:
    print("not multiple 7")