# Write a Python program to check whether a given key already exists in a dictionary.
def check_key_exits(key):
    if key in my_dict:
        print(f"The key {key} exits in the dictionary")
    else:
        print(f"The key {key} does not exits")

my_dict={"name":"gour","age":19,"city":"katwa","pin":713150}
key_dict=input("Enter the key to check::- ")
check_key_exits(key_dict)