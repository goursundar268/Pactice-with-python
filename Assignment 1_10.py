# Write a program Using a while loop to find and print the sum of all prime numbers less than or equal to n.

n = int(input("Enter a Number : "))
sum = 0
i = 2
while i<=n :
    j = 2
    isPrime = True
    while j<=(i//2) :
        if i%j==0 :
            isPrime = False
        j+=1
    if isPrime :
        sum+=i
    i+=1
print("Sum of All Prime Numbers from 1 to", n, "is :", sum)