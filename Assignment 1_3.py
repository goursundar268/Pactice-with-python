#Write A Program To Genrate And Print Tat First N Terms Of The Fibonacci Series Using Python.
x=int(input("Enter The Number"))
a=0
b=1
print(a)
print(b)
for i in range(x-2):
    b=a+b
    a=b-a
    print(b)