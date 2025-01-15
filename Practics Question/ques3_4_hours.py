# disc={} #empty dictionary

# sub1=input(str("Enter the first subject:"))
# sub2=input(str("Enter the second subject:"))
# sub3=input(str("Enter the third subject:"))
# disc={
#     "sub1":sub1,
#     "sub2":sub2,
#     "sub3":sub3
# }

# print(disc)

# two ways
marks={}
x=int(input("Entr the phy:"))
marks.update({"physics":x})

x=int(input("Entr the chem:"))
marks.update({"physics":x})

x=int(input("Entr the math:"))
marks.update({"physics":x})
print(marks)