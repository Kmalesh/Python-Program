with open("DEMO.txt","r") as f:
    # data=f.write("1,2,3,4,5,6,7,8")
    # print(data)
 
    
    data =f.read()
    print(data)

    num=""
    for i in range (len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]    
 

