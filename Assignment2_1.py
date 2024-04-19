int=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in int:
   if i%2==0:
        even.append(i)
        
   else :
      odd.append(i)
    
print("Even nyumber ara",even)
print("The size of even number",len(even))

print("Odd nyumber ara",odd)
print("The size of odd number",len(odd))
