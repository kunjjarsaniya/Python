import json
import random
import string
from pathlib import Path


class BankSystem:
    """
    A simple banking system using JSON file as storage.
    Supports account creation, deposit, withdrawal, detail viewing, update, and deletion.
    """

    database_file = 'data.json'
    user_data = []

    # Load existing data if the file exists
    try:
        if Path(database_file).exists():
            with open(database_file, 'r') as file:
                user_data = json.load(file)
        else:
            print("No existing data file found. Starting fresh.")
    except Exception as error:
        print(f"Error loading data: {error}")

    @classmethod
    def _save_data(cls):
        """Write current data to the JSON file."""
        with open(cls.database_file, 'w') as file:
            json.dump(cls.user_data, file, indent=4)

    @staticmethod
    def _generate_account_number():
        """
        Generate a random, unique account number with letters, digits, and a special character.
        Example format: aB1c2D!
        """
        letters = random.choices(string.ascii_letters, k=3)
        digits = random.choices(string.digits, k=3)
        special = random.choices("!@#$%^&*", k=1)
        account_number = letters + digits + special
        random.shuffle(account_number)
        return "".join(account_number)

    def create_account(self):
        """Create a new bank account."""
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        pin = input("Set a 4-digit PIN: ")

        if age < 18:
            print("Sorry, you must be at least 18 years old to create an account.")
            return
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN. Please enter a 4-digit number.")
            return

        new_account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "account_number": self._generate_account_number(),
            "balance": 0
        }

        BankSystem.user_data.append(new_account)
        BankSystem._save_data()

        print("✅ Account created successfully! Please note your account number:")
        for key, value in new_account.items():
            print(f"{key.capitalize()}: {value}")

    def _find_user(self, account_number, pin):
        """Find a user by account number and PIN."""
        return next((user for user in BankSystem.user_data if user['account_number'] == account_number and user['pin'] == pin), None)

    def deposit_money(self):
        """Deposit money into an account."""
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self._find_user(account_number, pin)

        if not user:
            print("❌ No matching account found.")
            return

        amount = int(input("Enter the amount to deposit: "))
        if not (0 < amount <= 10000):
            print("Invalid amount. You can deposit between 1 and 10,000.")
            return

        user['balance'] += amount
        BankSystem._save_data()
        print(f"✅ Amount deposited. New balance: ₹{user['balance']}")

    def withdraw_money(self):
        """Withdraw money from an account."""
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self._find_user(account_number, pin)

        if not user:
            print("❌ No matching account found.")
            return

        amount = int(input("Enter the amount to withdraw: "))
        if amount > user['balance']:
            print("❌ Insufficient funds.")
            return

        user['balance'] -= amount
        BankSystem._save_data()
        print(f"✅ Amount withdrawn. Remaining balance: ₹{user['balance']}")

    def view_details(self):
        """View account details."""
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self._find_user(account_number, pin)

        if not user:
            print("❌ No matching account found.")
            return

        print("\n🔍 Account Details:")
        for key, value in user.items():
            print(f"{key.capitalize()}: {value}")

    def update_details(self):
        """Update account holder's name, email, or PIN."""
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self._find_user(account_number, pin)

        if not user:
            print("❌ No matching account found.")
            return

        print("\nNote: You can't change age, account number, or balance.")
        name = input(f"Enter new name (leave blank to keep '{user['name']}'): ") or user['name']
        email = input(f"Enter new email (leave blank to keep '{user['email']}'): ") or user['email']
        new_pin = input("Enter new 4-digit PIN (leave blank to keep current): ")

        if new_pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = int(new_pin)
            else:
                print("Invalid PIN format. Keeping old PIN.")
                pin = user['pin']
        else:
            pin = user['pin']

        user.update({
            "name": name,
            "email": email,
            "pin": pin
        })

        BankSystem._save_data()
        print("✅ Details updated successfully.")

    def delete_account(self):
        """Delete an account permanently."""
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your PIN: "))
        user = self._find_user(account_number, pin)

        if not user:
            print("❌ No matching account found.")
            return

        confirmation = input("Are you sure you want to delete your account? (y/n): ").lower()
        if confirmation == 'y':
            BankSystem.user_data.remove(user)
            BankSystem._save_data()
            print("✅ Account deleted successfully.")
        else:
            print("❌ Account deletion cancelled.")


def main():
    bank = BankSystem()

    menu = """
    🔐 Bank System Menu
    -------------------------
    1. Create Account
    2. Deposit Money
    3. Withdraw Money
    4. View Account Details
    5. Update Account Details
    6. Delete Account
    -------------------------
    """

    print(menu)

    try:
        choice = int(input("Enter your choice (1-6): "))
        options = {
            1: bank.create_account,
            2: bank.deposit_money,
            3: bank.withdraw_money,
            4: bank.view_details,
            5: bank.update_details,
            6: bank.delete_account
        }
        if choice in options:
            options[choice]()
        else:
            print("Invalid option selected.")
    except ValueError:
        print("Please enter a valid number between 1 and 6.")


if __name__ == "__main__":
    main()
