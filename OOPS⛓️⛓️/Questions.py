'''Question:- Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
Apna College'''



class studentinfo:
    def __init__(self,name,marks):#Constuctor function
        self.name=name
        self.marks=marks
    
    def average(self):#simple function 
        sum=0
        for i in self.marks:
            sum+=i
        print("the Avarage of number is: ",(sum/3))

       

val=studentinfo("kamalesh kumar",[100,90,85])
print(val.name,val.marks)

val.average()


        