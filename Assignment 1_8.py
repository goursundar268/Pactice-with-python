# Write a program Using a for loop to print the square of each number from 1 to n.

num=int(input("Enter The Number:"))
print("Number \t \t Square")
for i in range(1,num+1):
    s=i**2
    print(f"{i} \t  \t {s}")