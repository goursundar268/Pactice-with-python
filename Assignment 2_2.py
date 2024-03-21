# Write a program in Python to create a list of integers then separate odd and even numbers from the given list.

list=[]
even=[]
odd=[]
while True:
    num=input("Enter The number(G for exit)::")
    if num=='g':
        break
    else:
        list.append(int(num))
for i in list:
   if i%2==0:
        even.append(i)
        
   else :
      odd.append(i)
    
print("Even nyumber ara",even)
print("The size of even number",len(even))

print("Odd nyumber ara",odd)
print("The size of odd number",len(odd))
