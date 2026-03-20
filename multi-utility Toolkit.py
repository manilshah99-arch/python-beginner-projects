print("Welcome to the muiti-utility Toolkit prohram.")
print("Description: ")
print("This program is build to display functions and operations of \ndifferent modules and packages")
import datetime
import math
import random
import string
import uuid

def datetime_menu():
    while True:
        print("\n--- Datetime Menu ---")
        print("1. Show current date & time")
        print("2. Difference between two dates")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("Current Date & Time:", now)

        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            try:
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

                diff = abs((date2 - date1).days)
                print("Difference:", diff, "days")
            except:
                print("Invalid date format!")

        elif choice == "3":
            break

def math_menu():
    while True:
        print("\n--- Math Menu ---")
        print("1. Square root")
        print("2. Factorial")
        print("3. Trigonometry (sin)")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            num = float(input("Enter number: "))
            print("Square root:", math.sqrt(num))

        elif choice == "2":
            num = int(input("Enter number: "))
            print("Factorial:", math.factorial(num))

        elif choice == "3":
            num = float(input("Enter angle in radians: "))
            print("Sin value:", math.sin(num))

        elif choice == "4":
            break

def random_menu():
    while True:
        print("\n--- Random Menu ---")
        print("1. Random number")
        print("2. Random password")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Random number:", random.randint(1, 100))

        elif choice == "2":
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits
            password = ''.join(random.choice(chars) for _ in range(length))
            print("Password:", password)

        elif choice == "3":
            break

def uuid_menu():
    print("\nGenerated UUID:")
    print(uuid.uuid4())

def file_menu():
    while True:
        print("\n--- File Menu ---")
        print("1. Write to file")
        print("2. Read file")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            data = input("Enter text: ")
            with open("output.txt", "a") as f:
                f.write(data + "\n")
            print("Saved!")

        elif choice == "2":
            try:
                with open("output.txt", "r") as f:
                    print("\nFile Content:\n", f.read())
            except FileNotFoundError:
                print("File not found!")

        elif choice == "3":
            break

def main():
    while True:
        print("\n=== Multi-Utility Toolkit ===")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
print("Thank You for using the python utility program.")
print("Goodbye.")