
import csv
import os

# File to store expense records
FILE_NAME = "expenses.csv"


# Load previously saved expenses
def load_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        print("Expense file not found. Starting with an empty expense list.")

    return expenses


# Save expenses to CSV file
def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "item", "category", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


# Add a new expense
def add_expense(expenses):
    print("\n--- Add New Expense ---")

    expense_date = input("Enter expense date (YYYY-MM-DD): ").strip()
    item = input("Enter item name: ").strip()
    category = input("Enter expense category: ").strip()

    # Validate expense amount
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break

        except ValueError:
            print("Invalid amount! Please enter a valid number.")

    # Create expense record
    expense = {
        "date": expense_date,
        "item": item,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    # Save updated expenses
    save_expenses(expenses)

    print("Expense added and saved successfully!")


# Display all expenses
def show_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses available.")
        return

    for expense in expenses:
        print(
            f"Date: {expense['date']} | "
            f"Item: {expense['item']} | "
            f"Category: {expense['category']} | "
            f"Amount: Rs. {float(expense['amount']):.2f}"
        )


# Calculate total expenses by category
def calculate_category_totals(expenses):
    print("\n--- Expenses by Category ---")

    if not expenses:
        print("No expenses available.")
        return

    # Set contains unique expense categories
    categories = {expense["category"] for expense in expenses}

    print("Unique Categories:", ", ".join(sorted(categories)))

    # Calculate total for each category
    for category in sorted(categories):
        total = sum(
            float(expense["amount"])
            for expense in expenses
            if expense["category"] == category
        )

        print(f"{category}: Rs. {total:.2f}")


# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n================================")
        print("     INSTITUTE EXPENSE TRACKER")
        print("================================")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            calculate_category_totals(expenses)

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


# Start the program
if __name__ == "__main__":
    main()
