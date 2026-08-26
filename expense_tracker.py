expense = {}
while True:
    print("What do you want to do?")
    print("1. Add Expense")
    print("2. List of all the expenses")
    print("3. Remove Expense")
    print("4. Check the Most Expensive Item")
    print("5. Total Expenses")
    print("6. Exit")

    choice = int(input("Enter your choice 1-6: "))

    if choice == 1:
        while True:
            item = input("Enter the name of the item: ")
            price = int(input("Enter the price of the item: "))

            expense[item] = price

            ask_again = input("Do you want to enter another expense? y/n: ").lower()

            while ask_again != "y" and ask_again != "n":
                print("Please enter y or n.")
                ask_again = input("Do you want to enter another expense? y/n: ").lower()

            if ask_again == "n":
                break

    elif choice == 2:
        if len(expense) == 0:
            print("No expenses found.")
        else:
            print("All Expenses:")
            for item, price in expense.items():
                print(item, ":", price)

    elif choice == 3:
        del_item = input("Enter item name to delete: ")

        if del_item in expense:
            del expense[del_item]
            print("Expense removed.")
        else:
            print("Item not found.")

    elif choice == 4:
        if len(expense) == 0:
            print("No expenses found.")
        else:
            highest_key = ""
            highest_value = 0

            for key, value in expense.items():
                if value > highest_value:
                    highest_value = value
                    highest_key = key

            print("Most expensive item:", highest_key)
            print("Price:", highest_value)

    elif choice == 5:
        print("Total expenses:", sum(expense.values()))

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Enter a number between 1-6.")
