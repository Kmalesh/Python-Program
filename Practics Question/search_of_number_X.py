num=[ 1,4,9,16,25,36,49,64,81,100]
i=0
f=0
x=int(input("Enter the X value:"))
while i<len(num):
    if num[i]==x:
        f=1  
        break
    i=i+1

if f==1:
    print("searching Found!")
else:
    print("NOT FOUND!")    

