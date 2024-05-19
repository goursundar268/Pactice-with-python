names = []
while True:
    print("******************")
    print("1.Display Item.")
    print("2.Search Item.")
    print("3.Add Item.")
    print("4.Delete Item.")
    print("5.Count Item.")
    print("6.Sort item.")
    print("7.Reverse Item.")
    print("8.Copy Items.")
    print("9.Exit")
    print("*******************")
    choice = int(input("Enter your Choice: "))
    
    if choice == 1:
        print(f"Names : {names}") #Display items
        
    elif choice == 2:
        search_name = input("Enter name you want to search:")
        if search_name in names:
            print(f"{search_name} is found at {names.index(search_name)+1}no. of Position.")
        else:
            print(f"{search_name} is not found in this list.")
            Choose = input("Do you want to save (yes/no): ")
            if Choose == 'yes':
                names.append(search_name)
                print("Saved Successfully.")
            else:
                print("Thank You for your opinion.")
            
    elif choice == 3:
        print("Write 'done' to finish Adding item.")
        while True:
            add_name = input(f"Enter the name to add items {"done to exit"} : ")
            if add_name == 'done':
                break
            else:
                names.append(add_name)
        print("Inserted Successfully.")
        
    elif choice == 4:
        delete_name = print("Enter name you want to delete:")
        names.remove(delete_name)
        
        
    elif choice == 5:
        print(f"Total number of items in the list: {len(names)}")
        
    elif choice == 6:
        sorted_list_asc = sorted(names) #Ascending Order
        print(f"Sorted list in Ascending order:{sorted_list_asc}")
        sorted_list_desc = sorted(names,reverse=True) #Descending Order
        print(f"Sorted list in Descending order:{sorted_list_desc}")
        
    elif choice == 7:
        reversed_list=names.reverse()
        print(f"Reversed list: {reversed_list} ")
        
    elif choice == 8:
        copy_of_names = names.copy()
        print(f"Copied List: {copy_of_names}")
        print("Copied Successfully.")
        
    else:
        print("Thank you")
        break
