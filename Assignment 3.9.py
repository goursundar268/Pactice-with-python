def check_key_exits(key):
    if key in my_dict:
        print(f"The key'{key}' exits in the dictionary")
    else:
        print(f"The key'{key}'does not exits")

my_dict={'name': 'Gour','age': 19,'city': 'katwa','pin':713150}
key_check=input("Enter the key to check:")
check_key_exits(key_check)