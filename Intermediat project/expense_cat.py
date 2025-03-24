import csv
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"

# load expenses
def load_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []
# categorize and plot expenses
def plot_expenses(expenses):
    categories = {}
    for row in expenses[1:]:
        _, category, _, amount = row
        categories[category] = categories.get(category, 0) + float(amount)
    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    plt.show()

# main function
def main():
    expenses = load_expenses()
    if expenses:
        plot_expenses(expenses)
    else:
        print("No expenses to display")

if __name__=="__main__":
    main()