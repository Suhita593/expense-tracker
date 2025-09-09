from db import init_db, add_expense, get_expenses
import datetime

# Think of this as showing "buttons" or options
def menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

# This line means: “If I run this file directly, start the program.”
if __name__ == "__main__":
    # First, we call init_db() → this creates the expenses database file if it doesn’t already exist.
    init_db()

    # This is a forever loop that keeps running until we quit
    while True:
        # Always show menu and wait for input
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/etc): ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.date.today().isoformat()  

            # calls add_expense and saves it in the database
            add_expense(amount, category, date)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = get_expenses()  # function call
            print("\n--- All Expenses ---")
            for exp in expenses:
                print(exp)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")