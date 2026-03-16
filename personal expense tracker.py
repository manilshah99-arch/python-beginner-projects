print("Welcome to the personal expense tracker program!")
print()
print("Description: ")
print("This program is built to track your weekly expenses.")
print()
expenses = []
name = input("Enter Your  Name: ")
print()

expense1 = int(input("Enter expense 1(in $): "))
expenses.append(expense1)
print()

expense2 = int(input("Enter expense 2(in $): "))
expenses.append(expense2)
print()

expense3 = int(input("Enter expense 3(in $): "))
expenses.append(expense3)
print()

expense4 = int(input("Enter expense 4(in $): "))
expenses.append(expense4)
print()

expense5 = int(input("Enter expense 5(in $): "))
expenses.append(expense5)

print()
expense6 = int(input("Enter expense 6(in $): "))
expenses.append(expense6)

print()
expense7 = int(input("Enter expense 7(in $): "))
expenses.append(expense7)

total_expenses = sum(expenses)
most_expensive = max(expenses)
cheapest_expense = min(expenses)
no_of_expenses = len(expenses)
avg_expense = total_expenses / no_of_expenses
uppercase_name = name.upper()
reversed_name = name[::-1]

print()
print("-----------WEEKLY EXPENSE REPORT-----------")
print()

print(f"Hello, {name}")
print(f"Name In Reversed Order: {reversed_name}")
print(f"Name In Uppercase: {uppercase_name}")
print()

print(f"No of expenses recorded: {no_of_expenses}")
print(f"Weekly Expenses: {expenses}")
print()
print(f"Total Expenses Of 7 Days: ${total_expenses}")
print(f"Most Expensive Expense: ${most_expensive}")

print(f"Cheapest Expense: ${cheapest_expense}")
print(f"Average expense in 7 days: ${avg_expense:.1f}")
