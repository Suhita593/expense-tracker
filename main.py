from db import db_init, add_expense, get_expenses
import datetime

#Think of these as the the buttons or list of options
def menu():
    print ("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


#This line means: “If I run this file directly, start the program.”
    if __name__ == "_main_":
        #First, we call init_db() → this creates the expenses database file if it doesn’t already exist.
        db_init()

#This is a forever loop that keeps running until we quit
        while True:

            #This always shows menu and waits for your input
            menu()
            choice = input("Enter choice")
            if choice == '1':
                amount = float(input("Enter amount: "))
                category = input("Enter category(Food/travel/etc): ")
                date = input("Enter date(YYYY-MM-DD) or Press Enter for today : ")
                if not date:
                    date = datetime.date.today().istoformat()
                    #calls add_expense and saves it in the database
                    add_expense(amount, category, date)
                    print("Expense added successfully!")

                elif choice == '2':
                    expenses = get_expenses
                    print("\n --- All Expenses ---")
                    for exp in expenses:
                        print(exp)

                elif choice == '3':
                    print ("Goodbye!")
                    break

                else :
                    print("Invalid choice. Please try again.")
