

import sqlite3



def init_db():
    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()


    cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               amount REAL,
               category TEXT,
               date TEXT
               )

""") 

    conn.commit()

    conn.close()



#the below function adds a new expense to the expenses table
def add_expense(amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
    conn.commit()
    conn.close()

#the below function fetches all rows from the expenses table
def get_expenses() :
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows