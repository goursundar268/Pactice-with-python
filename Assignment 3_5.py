def lcm(x,y):
    larger=max(x,y)
    for i in range(larger,x*y+1):
        if i % x==0 and i % y==0:
            return i
def gcd(x,y):
    lower=min(x,y)
    for i in range(lower,0,-1):
        if x % i==0 and y % i==0:
            return i

num1= int(input("Enter the first number::- "))
num2= int(input("Enter the second number::- "))

result=gcd(num1,num2)
print(f"The GCD of {num1} and {num2} is {result}")
print(f"The LCM of {num1} and {num2} is {lcm(num1,num2)}")