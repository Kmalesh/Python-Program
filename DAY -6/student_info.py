print("******FIVE_Student information of DP school******\n")

#user Defined functions (denods def)
def   school_detail():
    print("delhi public school")
    print("address:delhi")
    print("contact no:9728879312\n")
    
def student_1_information_input():
    # i=1
    # while i<=5:
    for i in range(4):
       name=input("Enter your name:")
       sub=int(input("Enter your Math Marks:"))
       sub2=int(input("Enter your hindi Marks:"))
       sub3=int(input("Enter your physics Marks:"))
       sub4=int(input("Enter your chemestry Marks:\n"))
       print("student name :",name)
       print("Math marks:",sub)
       print("Hindi marks:",sub2)
       print("physics marks:",sub3)
       print("chemistry marks:",sub4)
       school_detail()
    # i=i+1

student_1_information_input()