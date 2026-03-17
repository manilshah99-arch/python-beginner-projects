print("Welcome to the shopping list program!")
print()
print("Description: ")
print("This program is built to display:\n(1)List of items purchased.\n(2)Price of the most expensive item")
print("(3)Price of the cheapest item.\n(4)Total price of all items.")
print()
print()

items = []
prices = []

item1 = input("Enter the first item you want to buy: ")
price1 = int(input("Enter the price of the first item(in $): "))
items.append(item1)
prices.append(price1)

print()

item2 = input("Enter the second item you want to buy: ")
price2 = int(input("Enter the price of the second item(in $): "))
items.append(item2)
prices.append(price2)

print()

item3 = input("Enter the third item you want to buy: ")
price3 = int(input("Enter the price of the third item(in $): "))
items.append(item3)
prices.append(price3)

print()

item4 = input("Enter the fourth item you want to buy: ")
price4 = int(input("Enter the price of the fourth item(in $): "))
items.append(item4)
prices.append(price4)

print()

item5 = input("Enter the fifth item you want to buy: ")
price5 = int(input("Enter the price of the fifth item(in $): "))
items.append(item5)
prices.append(price5)

print()

most_expensive = max(prices)
least_expensive = min(prices)
total_price = sum(prices)
print("---------Here's Your Shopping Cart---------")
print()
print(f"List of items purchased: {items}")
print(f"Price of the most expensive item: {most_expensive}$")
print(f"Price of the least expensive item: {least_expensive}$")
print(f"Here\'s your total bill: {total_price}$")

print()
print("Thank you for shopping through our shopping mall!")
print("Have a good day.\nSee you soon!")