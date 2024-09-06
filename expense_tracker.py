expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., food, transport): ")
        description = input("Enter a brief description: ")
        expenses.append({"amount": amount, "category": category, "description": description})
        print("Expense added!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']} - RS{expense['amount']}: {expense['description']}")

def main_menu():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
