from db import init_db, add_expense, get_expenses
import datetime
import reports 


def menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


if __name__ == "__main__":
    # Initialize the database
    init_db()

    while True:
       
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/etc): ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.date.today().isoformat()  

           
            add_expense(amount, category, date)
            print("Expense added successfully!")

        elif choice == "2":
            expenses = get_expenses()  
            print("\n--- All Expenses ---")
            for exp in expenses:
                print(exp)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")