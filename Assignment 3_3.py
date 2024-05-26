# Write a PYTHON program to calculate the Fibonacci series using function.
a,b=0,1
listt=[0,]
def fibonacci():
    x=1
    while x!=0:
        x=int(input("Enter 'g' for break::- "))
        global a,b
        listt.append(b)
        a,b=b,a+b
        print(f"\n The Fibonacci Series is {listt}\n")
fibonacci()