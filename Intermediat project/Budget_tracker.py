import json

FILENAME = 'budget.json'

def load_budget():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": [], "expenses": []}

def save_budget(budget):
    with open(FILENAME, 'w') as file:
        json.dump(budget, file)

def add_entry(budget, entry_type):
    amount = float(input(f"Enter {entry_type} amount"))
    budget[entry_type].append(amount)
    save_budget(budget)
    print(f"{entry_type.capitalize()} recorded!")

def display_budget(budget):
    total_income = sum(budget['income'])
    total_expenses = sum(budget['expenses'])
    balance = total_income - total_expenses
    print(f"\nTotal income: ${total_income}")
    print(f"\nTotal expenses: ${total_expenses}")
    print(f"\nBalance: ${balance:.2f}")


def main():
    budget = load_budget()

    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Budget")
        print("4. Exit")
        choice = input("choose an option: ")

        if choice == "1":
            add_entry(budget, "income")
        elif choice == "2":
            add_entry(budget, "expenses")
        elif choice == "3":
            display_budget(budget)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()