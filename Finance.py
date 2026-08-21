import calendar
expense = []
print("WELCOME TO EXPENSE TRACKER 💰")
while True:
    print("\n======= MENU =======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Spending")
    print("4. Exit")
    print("====================")
    choice = input("Choice (1-4): ")
    # 1. Add Expense
    if choice == "1":
        print(calendar.calendar(2026))
        date = input("Enter the Date (DD/MM/YYYY): ")
        category = input("Enter the Category of Expense: ")
        description = input("Enter a Short Description: ")
        amount = int(input("Enter the Amount (₹): "))
        expense_list = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount        }
        expense.append(expense_list)
        print("\n✅ Expense Added Successfully!")
    # 2. View All Expenses
    elif choice == "2":
        if len(expense) == 0:
            print("\nNo Expenses Added.")
        else:
            print("\n====== ALL EXPENSES ======")
            count = 1
            for each_expense in expense:
                print(
                    f"{count}. "
                    f"Date: {each_expense['Date']}, "
                    f"Category: {each_expense['Category']}, "
                    f"Description: {each_expense['Description']}, "
                    f"Amount: ₹{each_expense['Amount']}"
                )
                count += 1
    # 3. Total Spending
    elif choice == "3":
        total = 0
        for each_expense in expense:
            total += each_expense["Amount"]
        print(f"\nTOTAL SPENDING = ₹{total}")
    # 4. Exit
    elif choice == "4":
        print("Thank You!")
        break
    # Invalid Choice
    else:
        print("Invalid Choice! Please try again.")