#	Write a PYTHON program to check whether a number is prime or not using function.

#funcution are here:
def chack_prime(number):
    f=0
    for i in range(2,number):
        if number%i==0:
            f=1
            break
    if(f==0):
        print(num,"The Number is a Prime")
    else:
        print(num,"The number is a Not Prime")

# main funcation are here::
num=int(input("Enter a Number::"))
chack_prime(num)