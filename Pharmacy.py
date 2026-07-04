med = []

while True:
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Find Medicine")
    print("4. Update Stock")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("name: ")
        price = int(input("price: "))
        stock = int(input("stock: "))

        med.append({"name": name, "price": price, "stock": stock})
        


    elif choice == "2":
        for m in med:
            print(m["name"])
            print(m["price"])
            print(m["stock"])
            print("----------")

    elif choice == "3":
        search = input("enter name to find")
        for m in med:
            if m["name"] == search:
                print("found")
                print("Name:", m["name"])
                print("Price:", m["price"])
                print("Stock:", m["stock"])
            else:
                print("medicine not found")
    elif choice == "4":
        search=input("enter medicine name")
        for i in med:
            if i["name"]==search:
                print("current stock",i["stock"])
                new_stock=(input("new stock"))
                i["stock"]=new_stock
                print("found")
                print("Name:", i["name"])
                print("Price:", i["price"])
                print("Stock:", i["stock"])
                break
        else:   
             print("medicine not found")

                


    elif choice == "5":
        break

    else:
        print("Invalid choice")