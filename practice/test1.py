import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class BankManagementSystem:
    def __init__(self, file_name: str = "bank_accounts.json"):
        self.file_name = file_name
        self.accounts: List[Dict] = []
        self.next_account_number = 1001
        self.load_data()

    def load_data(self) -> None:
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    data = json.load(file)
                self.accounts = data.get("accounts", [])
                self.next_account_number = data.get("next_account_number", 1001)
            except json.JSONDecodeError:
                self.accounts = []
                self.next_account_number = 1001
        else:
            self.accounts = []
            self.next_account_number = 1001

    def save_data(self) -> None:
        data = {
            "next_account_number": self.next_account_number,
            "accounts": self.accounts,
        }
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=2)

    def get_account(self, account_number: str) -> Optional[Dict]:
        for account in self.accounts:
            if account["account_number"] == account_number:
                return account
        return None

    def create_account(self, name: str, pin: str, initial_deposit: float) -> Dict:
        if not name.strip():
            raise ValueError("Customer name cannot be empty.")
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        account_number = f"ACC{self.next_account_number}"
        self.next_account_number += 1

        account = {
            "account_number": account_number,
            "customer_name": name.strip().title(),
            "pin": pin,
            "balance": round(initial_deposit, 2),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "transactions": [
                {
                    "type": "opening_balance",
                    "amount": round(initial_deposit, 2),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ],
        }
        self.accounts.append(account)
        self.save_data()
        return account

    def deposit(self, account_number: str, pin: str, amount: float) -> Dict:
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        if account["pin"] != pin:
            raise ValueError("Incorrect PIN.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        account["balance"] = round(account["balance"] + amount, 2)
        account["transactions"].append(
            {
                "type": "deposit",
                "amount": round(amount, 2),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.save_data()
        return account

    def withdraw(self, account_number: str, pin: str, amount: float) -> Dict:
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        if account["pin"] != pin:
            raise ValueError("Incorrect PIN.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if account["balance"] < amount:
            raise ValueError("Insufficient balance.")

        account["balance"] = round(account["balance"] - amount, 2)
        account["transactions"].append(
            {
                "type": "withdraw",
                "amount": round(amount, 2),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.save_data()
        return account

    def transfer(self, sender_account: str, sender_pin: str, receiver_account: str, amount: float) -> Dict:
        sender = self.get_account(sender_account)
        receiver = self.get_account(receiver_account)

        if not sender:
            raise ValueError("Sender account not found.")
        if not receiver:
            raise ValueError("Receiver account not found.")
        if sender["pin"] != sender_pin:
            raise ValueError("Incorrect sender PIN.")
        if sender_account == receiver_account:
            raise ValueError("Sender and receiver accounts cannot be the same.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if sender["balance"] < amount:
            raise ValueError("Insufficient balance for transfer.")

        sender["balance"] = round(sender["balance"] - amount, 2)
        receiver["balance"] = round(receiver["balance"] + amount, 2)

        sender["transactions"].append(
            {
                "type": "transfer_sent",
                "amount": round(amount, 2),
                "to_account": receiver_account,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        receiver["transactions"].append(
            {
                "type": "transfer_received",
                "amount": round(amount, 2),
                "from_account": sender_account,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.save_data()
        return {"sender": sender, "receiver": receiver}

    def check_balance(self, account_number: str, pin: str) -> float:
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        if account["pin"] != pin:
            raise ValueError("Incorrect PIN.")
        return account["balance"]

    def get_transaction_history(self, account_number: str, pin: str) -> List[Dict]:
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        if account["pin"] != pin:
            raise ValueError("Incorrect PIN.")
        return account["transactions"]

    def view_all_accounts(self) -> List[Dict]:
        return sorted(self.accounts, key=lambda x: x["account_number"])

    def delete_account(self, account_number: str, admin_pin: str) -> str:
        if admin_pin != "admin123":
            raise ValueError("Admin PIN is incorrect.")
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found.")
        self.accounts.remove(account)
        self.save_data()
        return f"Account {account_number} deleted successfully."


def print_menu() -> None:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Transaction History")
    print("6. Transfer Money")
    print("7. View All Accounts (Admin)")
    print("8. Delete Account (Admin)")
    print("9. Exit")
    print("================================")


def main() -> None:
    bank = BankManagementSystem("bank_accounts.json")
    print("Bank system loaded successfully.")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter customer name: ").strip()
                pin = input("Enter 4-digit PIN: ").strip()
                amount = float(input("Enter initial deposit: "))
                account = bank.create_account(name, pin, amount)
                print(f"Account created successfully. Your account number is: {account['account_number']}")

            elif choice == "2":
                account_number = input("Enter account number: ").strip()
                pin = input("Enter PIN: ").strip()
                amount = float(input("Enter deposit amount: "))
                account = bank.deposit(account_number, pin, amount)
                print(f"Deposit successful. New balance: {account['balance']}")

            elif choice == "3":
                account_number = input("Enter account number: ").strip()
                pin = input("Enter PIN: ").strip()
                amount = float(input("Enter withdrawal amount: "))
                account = bank.withdraw(account_number, pin, amount)
                print(f"Withdrawal successful. New balance: {account['balance']}")

            elif choice == "4":
                account_number = input("Enter account number: ").strip()
                pin = input("Enter PIN: ").strip()
                balance = bank.check_balance(account_number, pin)
                print(f"Current balance: {balance}")

            elif choice == "5":
                account_number = input("Enter account number: ").strip()
                pin = input("Enter PIN: ").strip()
                history = bank.get_transaction_history(account_number, pin)
                print("Transaction history:")
                for item in history:
                    print(item)

            elif choice == "6":
                sender_account = input("Enter sender account number: ").strip()
                sender_pin = input("Enter sender PIN: ").strip()
                receiver_account = input("Enter receiver account number: ").strip()
                amount = float(input("Enter transfer amount: "))
                result = bank.transfer(sender_account, sender_pin, receiver_account, amount)
                print(
                    f"Transfer successful. {amount} transferred from {sender_account} to {receiver_account}."
                )
                print(f"Sender balance: {result['sender']['balance']}")
                print(f"Receiver balance: {result['receiver']['balance']}")

            elif choice == "7":
                admin_pin = input("Enter admin PIN: ").strip()
                if admin_pin != "admin123":
                    print("Invalid admin PIN.")
                    continue
                accounts = bank.view_all_accounts()
                print("All accounts:")
                for account in accounts:
                    print(
                        f"{account['account_number']} | {account['customer_name']} | Balance: {account['balance']}"
                    )

            elif choice == "8":
                account_number = input("Enter account number to delete: ").strip()
                admin_pin = input("Enter admin PIN: ").strip()
                print(bank.delete_account(account_number, admin_pin))

            elif choice == "9":
                print("Thank you for using the Bank Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
