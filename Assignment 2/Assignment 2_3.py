lst=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        lst.append(int(num))
x=int(input("The element of seach:"))
if x in lst:
    print("this number is found in this list")
else:
    print("this number is not found in this list")
    