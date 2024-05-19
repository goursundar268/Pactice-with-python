
#funcation 
def addition (number1,Number2):
    chose=number1+Number2
    print("the finle answer is",chose)
    
def subtrucition (number1,Number2):
    chose=number1+Number2
    print("the finle answer is",chose)
    
    
def Multiply (number1,Number2):
    chose=number1+Number2
    print("the finle answer is",chose)
    
    
def Divison (number1,Number2):
    chose=number1+Number2
    print("the finle answer is",chose)

#main funcation here
one1=int(input("Enter a number1::"))
one2=int(input("Enter a number2::"))

choice=int(input("\n prass 1:(Addition) \n pass 2:(subtrucition) \n pass 3:(Multiply) \n pass 4:(Divison)\n Enter the choice:: "))

if choice==1:
    addition(one1,one2)
elif choice==2:
    subtrucition(one1,one2)
elif choice==3:
    Multiply(one1,one2)
elif choice==4:
    Divison(one1,one2)
