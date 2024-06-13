even=[]
odd=[]
for i in range(1,101):
    print(i ,end=" ,")
    if i%2==0:
        even.append(i)
        
    else :
      odd.append(i)
print()    
print("Even nyumber are",even)
print("The size of even number",len(even))

print("Odd nyumber are",odd)
print("The size of odd number",len(odd))
