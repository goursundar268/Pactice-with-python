#Write A Program To Calculate And Print The Factorial
n=int(input("Enter the Number"))
result=1
for i in range(n,0,-1):
    result=result*i
print(f"The Factorial Of {n} is {result}")
