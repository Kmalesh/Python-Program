class student:
    #default constructor
    def __init_subclass__(cls):
        pass


#parameter constuctor
    def __init__(self,name,marks,rollno):
        self.name=name
        self.marks=marks
        self.rollno=rollno

ob=student('kamlesh kumar\n',100,1323407)
print(ob.name,ob.marks,ob.rollno)
        