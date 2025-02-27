f=open("DEMO.txt","a")# append the heloo



# data=f.read()
# print(data)

data=f.write(" heloooo")
print(data)
f.close()


f=open("practics.txt","w")#file create
f=open("practics.txt","r+")#📍 r+ se read and write dono 

# data=f.write("hello my name  is kamalesh kumar")
# print(data)
dat=f.read()
print(dat)
f.close()