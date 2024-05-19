def gcd(num1,num2):
    if num1>num2:
        for i in range(num1,0,-1):
            if num1 % i==0 and num2 % i==0:
                break
        print(f"A number of gcd::{i}")
    else:
        for i in range(num2,0,-1):
            if num1 % i==0 and num2 % i==0:
                break
        print(f"A number of gcd::{i}")
            

    
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
gcd(num1,num2)