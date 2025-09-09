# this is a database helper file that manages all interactions with the SQLite database.

import sqlite3

#this function initializes the database and creates the expenses table if it does not exists

def init_db():
    conn = sqlite3.connect("expenses.db")
#the above code opens a connection to the SQLite database file named "expenses.db". If the file does not exist, it will be created. conn is like a bridge between your python code and and database file.
    cursor = conn.cursor()
# A cursor is an object that lets you execute the SQL commands 

    cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               amount REAL,
               category TEXT,
               date TEXT
               )

""") 

    conn.commit()
#saves changes to the database file.
    conn.close()
#ends the connection to the database file.


#the below function adds new expense to the database
#in the below code ? are placeholders - this prevent SQL injection and makes it secure
#(amount, category, date) are the actual values passed when you call the function
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