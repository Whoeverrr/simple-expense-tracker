#importing CSV module
import csv

#Creating a constant variable to the name of the csv file
FILENAME = "expenses.csv"
IncomeFILENAME = "income.csv"

#define add expense function
def add_expense():
    #amount, category and description is equal to the user input 
    amount = input("Enter any amount: R")
    category = input("Enter category of expense (e.g. Food, Entertainment, Rent): ")
    description = input("Enter description: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
        print("Expense added!\n")
    get_confirmation()  

#defining confirmation function
def get_confirmation():
    while True:
        confirmation = input("Return to main menu ?(Press 'y' for yes and 'n' for no): ").lower().strip()
        if confirmation == "y":
            menu()
        elif confirmation == "n":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Press 'y' for yes and 'n' for no")

#define view expense fuction
def view_expense():
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.reader(file)
            total = 0
            print("\n--- All expenses ---")
            for row in reader:
                try:
                    print(f"R{row[0]}|{row[1]}|{row[2]}")
                    total += float(row[0])
                    print(f"\nTotal Spent: R{total}")
                except (ValueError, IndexError):
                    print("Skipping Invalid row:", row)
    except FileNotFoundError:
        print("No expenses found yet.")
    get_confirmation()   

#defining view Income function
def view_income():
    try:
        with open(IncomeFILENAME, mode="r") as file:
            reader = csv.reader(file)
            total = 0
            print("\n--- Income Tracker ---")
            for row in reader:
                try:
                    print(f"R{row[0]}|{row[1]}|{row[2]}")
                    total += float(row[0])
                    print(f"\nTotal Earned: R{total}")
                except (ValueError, IndexError):
                    print("Skipping invalid row:", row)
    except FileNotFoundError:
        print("No income stated yet.")
    get_confirmation()  

#defining income function
def add_income():
    #amount, category and description is equal to the user input 
    amount = input("Enter any amount: R")
    category = input("Enter category of income (e.g. Salary, Investment, Side Hustle): ")
    description = input("Enter description: ")

    with open(IncomeFILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
        print("Income added!\n")
    get_confirmation()  

#defining a looping menu fuction
def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        print("")
        print("\n=== Income Tracker ===")
        print("4. Add Income")
        print("5. View Income")
        print("6. Exit")

        choice = input("Choose and option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            print("Thank you for using the app. Goodbye.")
        elif choice == "4":
            add_income()
        elif choice == "5":
            view_income()
        elif choice == "6":
            print("Thank you for using the app. Goodbye.")
            break
        else:
            print("Invalid Choice!\n")

#Run the app using menu fuction
menu()
    