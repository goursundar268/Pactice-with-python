def count_value(value,dict):
    c=0
    for i in dict.values():
        if i==value:
            c+=1

    if c>0:
        print(f"The value {value} exit in dictionary for {c} keys")
    else:
        print(f"The values {value} does not exits in the dictionary")
        

my_dict={"name":"gour","age":19,"city":"katwa","pin":713150}
values=input("enter the value to chack:- ")
count_value(values,my_dict)