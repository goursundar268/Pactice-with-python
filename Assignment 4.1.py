fp=open("std_rec.txt","w")
num=int(input("Enter Number of Students:- "))

for i in range(num):
    print("student",(i+1))
    std_name=input("Enter name:- ")
    std_roll=input("Enter Roll:- ")
    std_marks=input("Enter Marks:- ")
    std_rec=[std_name, "\t", std_roll, "\t", std_marks,"\n"]

    fp.writelines(std_rec)
    print("\n")