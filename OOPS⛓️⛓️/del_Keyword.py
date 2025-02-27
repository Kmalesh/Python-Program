class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

s1=student("kamalesh kumar",1323407)    
print(s1.name) 
print(s1.rollno) 

del s1   # delete object 
print(s1.name)  # not work because s1 object is deleted
print(s1.rollno) 