import random
a=random.randint(1,25)
atempt=0
while atempt<5:
    print("remaining atempt are",(5-atempt))
    guess=int(input("Guess a number::"))
    if a==guess:
        print("Wow!!!!!! your guess is right")
        break
    elif a>guess:
        print("Chose some lager number")
        atempt=atempt+1
    else:
        print("Chose some smaller number")
        atempt=atempt+1
if(atempt==5):
    print("Sorry your guess is wrong")
    print("The number is ::,",a)