print("Welcome to the file operator program!")
print("Description: ")
print("This program is built to allow user to maintain personal journal.")
import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}] {entry}\n")
            print("Entry added successfully!\n")
        except Exception as e:
            print(" Error while writing to file:", e)

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()
                if data:
                    print("\nYour Journal Entries:\n")
                    print(data)
                else:
                    print("No entries found.\n")
        except FileNotFoundError:
            print("File not found. No entries yet.\n")

    def search_entries(self):
        keyword = input("Enter keyword to search: ")

        try:
            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching entries found.\n")
        except FileNotFoundError:
            print("File not found.\n")

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("All entries deleted.\n")
                else:
                    print("No file to delete.\n")
            except Exception as e:
                print("Error deleting file:", e)
        else:
            print("Deletion cancelled.\n")


def main():
    journal = JournalManager()

    while True:
        print("====== Personal Journal Manager ======")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entries()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

print()
print("Thank you for using the file operator program!")
print("Goodbye.")