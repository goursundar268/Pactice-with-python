item={}
while True:
    print("1.for add item")
    print("2.for update item")
    print("3.for display")
    print("4.for item count")
    print("5. for delete")
    print("6. for search")
    print("7. for sorted items")
    print("0. exit")
    ch=int(input("Enter your choice:: "))
    if ch==1:
        item_name=input("Enterr item name::")
        price=int(input("Enter item price"))
        item[item_name]=price
        print(f"{item_name} is add")
    elif ch==2:
        name=input("Enter item name::")
        if name in item.keys():
            price=int(input("Enter price::"))
            item[name]=price
        else:
            print(f"{name} is not found")
    elif ch==3:
        for i in item:
            print(f"{i}-------->{item[i]}")
    elif ch==4:
        print(f"Total  number of item{len(item)}")

    elif ch==5:
        name=input("Enter item name::")
        if name in item:
            del item[name]
            print(f"{name} is removed")
        else:
            print("item is not found")
    
    elif ch==6:
        name=input("Enter name::")
        for i in item:
            if i==name:
                print(f"{i}:{item[i]}")
                break
        else:
            print("item is not found")
    
    elif ch==7:
        sort_item=sorted(item.keys())
        for i in sort_item:
            print(f"{i}  is sorted from{sorted}")

    elif ch==0:
        print("thank you")
        break
    else:
        print("Enter a valid option")
