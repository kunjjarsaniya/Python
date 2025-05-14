
# 🏦 Python Banking System

A beginner-friendly, object-oriented Python project for managing basic bank operations using file handling and a simple JSON database.

## 📂 Features

- Create a new account with name, age, email, and PIN.
- Deposit and withdraw money.
- View account details.
- Update account information.
- Delete an account.

## 🧱 Technologies Used

- Python 3
- JSON (for data storage)
- `pathlib` for file path handling
- Random string generation for account numbers

## 📁 Data Structure

Accounts are stored in a `data.json` file as a list of dictionaries. Each account includes:

```json
{
  "name": "John Doe",
  "age": 25,
  "email": "john@example.com",
  "pin": 1234,
  "account_number": "A1b2C3!",
  "balance": 0
}
```

## 🧠 How it Works

### 1. Account Creation
- Validates age (must be ≥ 18)
- PIN must be a 4-digit number
- Random account number is generated

### 2. Deposit & Withdraw
- Validates account and PIN
- Deposit amount must be between ₹1 and ₹10,000
- Withdraw amount must not exceed balance

### 3. Update Details
- Allows updating name, email, and PIN
- Age, account number, and balance are not editable

### 4. Delete Account
- Requires confirmation
- Deletes account from JSON and updates file

## 🚀 Getting Started

Run the script and follow the menu prompts:

```bash
python banking_system_project.py
```

## 🛡 Suggestions for Improvement

- Use hashed PINs for security
- Switch to SQLite or MySQL for data storage
- Add a user-friendly GUI with `tkinter` or a web version with Flask