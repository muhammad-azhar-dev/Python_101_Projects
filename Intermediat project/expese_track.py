import csv
from datetime import datetime

# file name for storing expeses
FILENAME = 'expeses.csv'

# function to add an expense
def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Travel): ")
        description = input("Enter a short description: ")
        amount = float(input("Enter the amount: "))

        # save expense to csv file
        with open(FILENAME, mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount, please enter  a valid number.")
    


# function to view expenses
def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            print(f"{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':<10}")
            print("_"*65)
            for row in reader:
                print(f"{row[0]:<12} {row[1]:<15} {row[2]:<25} {row[3]:<10}")
    except FileNotFoundError:
        print("No expeses found. Start by adding some.")


# main menu
def main():
    while True:
        print("\nExpense Tracher")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Good bye!")
            break
        else:
            print("Invalid choice. please try again.")

#run the program
if __name__ == "__main__":
    main()
