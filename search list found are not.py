list=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        list.append(int(num))
x=int(input("The element of seach:"))
if num in list:
    print("the number of found of this list")
else:
    print("the number of not found of this list")
    