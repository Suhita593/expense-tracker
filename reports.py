
#Helps us talk to the expenses database
import sqlite3

#plt - drawing tool in python, used here to make a pie chart
import matplotlib.pyplot as plt

def category_report():
    conn = sqlite3.connect('expenses.db')

    #cursor is like a pen that helps you read/write inside a database
    cursor = conn.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    conn.close()

    #Prepare data for chart
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    #Creating the pie chart
    plt.pie(amounts, labels= categories, autopct= '%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()
