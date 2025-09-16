
import sqlite3

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def category_report():
    conn = sqlite3.connect('expenses.db')

    
    cursor = conn.cursor()

    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    print(data)

    conn.close()

    #Prepare data for chart
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    #Creating the pie chart
    plt.pie(amounts, labels= categories, autopct= '%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

if __name__ == "__main__":
    category_report()
