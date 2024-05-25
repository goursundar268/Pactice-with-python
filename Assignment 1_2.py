#Write A proram To Demonstrate Different Data Type In Python
manu={
    "1" : "Addition",
    "2" : "Substration",
    "3" : "maltiplication",
    "4" : "Division",
    "5" : "Reminder",
    "6" : "Quotient",
    "7" : "Exporent"
}
for i in manu:
    print(i,manu[i])
ch=int(input("Enter The choice::"))
a=int(input("Enter The Nmuber 1::"))
b=int(input("Enter The Number 2::"))

if ch==1:
    r1=a+b
    print(f"Addition of {a} and {b} is {r1}")
elif ch==2:
    r1=a-b
    print(f"Substration of {a} and {b} is {r1}")
elif ch==3:
    r1=a*b
    print(f"maltiplication of {a} and {b} is {r1}")
elif ch==4:
    r1=a/b
    print(f"Division of {a} and {b} is {r1}")
elif ch==5:
    r1=a%b
    print(f"Reminder of {a} and {b} is {r1}")
elif ch==6:
    r1=a//b
    print(f"Quotient of {a} and {b} is {r1}")
elif ch==7:
    r1=a**b
    print(f"Exponentent of {a} and {b} is {r1}")
else:
    print("sorry:: wrong operatar")
print("thnak you using it \n this is created by gour")