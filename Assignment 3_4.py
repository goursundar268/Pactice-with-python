# Write a PYTHON program to swap two numbers by call by value and call by address.
def swap_num(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
a=int(input("Enter the first Number::- "))
b=int(input("Enter the Second Number::- "))
a,b=swap_num(a,b)

print(a,b)