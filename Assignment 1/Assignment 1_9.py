# Write a python program to print the following pattern-

i=int(input("Enter The of rows::"))
for i in range(1,i+1):
    for j in range(1,i+1):
        print(f"{"*"}",end="")
    print("")

for i in range(1,6):
    for j in range(1,i+1):
        print(f"{j}",end="")
    print("")

for i in range(1,i+1):
    for j in range(i):
        print(chr(j+65),end="")
    print("")

for i in range(1,i+1):
    for j in range(i):
        print(chr(j+97),end="")
    print("")