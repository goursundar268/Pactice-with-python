#Write A Program To Python If Number Is Positive, Chack If It Prime Number
num=int(input("Enter The Number:"))
f=0
if num>0:
    for i in range(1,num+1):
        if num%i==0:
         f=f+1
    if f==2:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")
else:
   print(f"{num} is not positive number")