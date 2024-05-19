lst=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        lst.append(int(num))
x=int(input("The element of seach:"))
if num in lst:
    print("the number of found of this list")
else:
    print("the number of not found of this list")
    
    y=int(input("Add element yes(1)/No(0)::"))
    if y==1:
        lst.append(y)
        print("Add succesfully")
        print(lst)
    elif y==0:
        lst.append(y)
        print("no Added")
       
    else:
        print("Invild")
        
    