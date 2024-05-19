def fact(done):
    result=1
    for i in range(done,0,-1):
        result=result*i
    print(f" the factorial of {done} is {result}")
        
num=int(input("Enter a number:"))
fact(num)