#	Write a program to Implement a while loop to repeatedly ask the user for a number until they enter a negative number. For each entered positive number, calculate and print its factorial.


while True:
    fact=1
    num=int(input("Enter The Number:"))
    if num>=0:
        for i in range(1,num+1):
            fact=fact*i
        print(f"factorial of {num} is {fact}")
    else:
        print("Enter you negitive Number")
        break