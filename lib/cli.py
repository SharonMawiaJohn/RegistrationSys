from models import session
from helpers import (
    create_customer, update_customer, delete_customer, list_customers,
    find_customer_by_name, find_customer_by_id, create_account, update_account,
    delete_account, list_accounts, find_account_by_number, find_account_by_id,
    create_transaction, update_transaction, delete_transaction, find_transaction_by_id,
    create_loan, update_loan, delete_loan, find_loan_by_id,
    list_customer_accounts, list_customer_loans, list_account_transactions,
    exit_program
)

def main_menu():
    """Main menu for the banking application."""
    while True:
        print("\n--- Main Menu ---")
        print("1: Customer Options")
        print("2: Account Options")
        print("3: Transaction Options")
        print("4: Loan Options")
        print("5: List All Options")
        print("0: Exit")
        
        choice = input("> ")
        
        if choice == "1":
            customer_menu()
        elif choice == "2":
            account_menu()
        elif choice == "3":
            transaction_menu()
        elif choice == "4":
            loan_menu()
        elif choice == "5":
            list_all_menu()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

# Customer Options
def customer_menu():
    """Menu for customer-related operations."""
    while True:
        print("\n--- Customer Options ---")
        print("1: Create customer")
        print("2: Update customer")
        print("3: Delete customer")
        print("4: List customers")
        print("5: Find customer by name")
        print("6: Find customer by ID")
        print("0: Back to Main Menu")

        choice = input("> ")

        if choice == "1":
            create_customer(session)
        elif choice == "2":
            update_customer(session)
        elif choice == "3":
            delete_customer(session)
        elif choice == "4":
            list_customers(session)
        elif choice == "5":
            find_customer_by_name(session)
        elif choice == "6":
            find_customer_by_id(session)
        elif choice == "0":
            return  # Go back to main menu
        else:
            print("Invalid choice. Please try again.")

# Account Options
def account_menu():
    """Menu for account-related operations."""
    while True:
        print("\n--- Account Options ---")
        print("7: Create account")
        print("8: Update account")
        print("9: Delete account")
        print("10: List accounts")
        print("11: Find account by number")
        print("12: Find account by ID")
        print("0: Back to Main Menu")

        choice = input("> ")

        if choice == "7":
            create_account(session)
        elif choice == "8":
            update_account(session)
        elif choice == "9":
            delete_account(session)
        elif choice == "10":
            list_accounts(session)
        elif choice == "11":
            find_account_by_number(session)
        elif choice == "12":
            find_account_by_id(session)
        elif choice == "0":
            return  # Go back to main menu
        else:
            print("Invalid choice. Please try again.")

# Transaction Options
def transaction_menu():
    """Menu for transaction-related operations."""
    while True:
        print("\n--- Transaction Options ---")
        print("13: Create transaction")
        print("14: Update transaction")
        print("15: Delete transaction")
        print("16: Find transaction by ID")
        print("0: Back to Main Menu")

        choice = input("> ")

        if choice == "13":
            create_transaction(session)
        elif choice == "14":
            update_transaction(session)
        elif choice == "15":
            delete_transaction(session)
        elif choice == "16":
            find_transaction_by_id(session)
        elif choice == "0":
            return  # Go back to main menu
        else:
            print("Invalid choice. Please try again.")

# Loan Options
def loan_menu():
    """Menu for loan-related operations."""
    while True:
        print("\n--- Loan Options ---")
        print("17: Create loan")
        print("18: Update loan")
        print("19: Delete loan")
        print("20: Find loan by ID")
        print("0: Back to Main Menu")

        choice = input("> ")

        if choice == "17":
            create_loan(session)
        elif choice == "18":
            update_loan(session)
        elif choice == "19":
            delete_loan(session)
        elif choice == "20":
            find_loan_by_id(session)
        elif choice == "0":
            return  # Go back to main menu
        else:
            print("Invalid choice. Please try again.")

# List All Options
def list_all_menu():
    """Menu for listing all accounts, loans, and transactions."""
    while True:
        print("\n--- List All Options ---")
        print("21: List customer accounts")
        print("22: List customer loans")
        print("23: List account transactions")
        print("0: Back to Main Menu")

        choice = input("> ")

        if choice == "21":
            list_customer_accounts(session)
        elif choice == "22":
            list_customer_loans(session)
        elif choice == "23":
            list_account_transactions(session)
        elif choice == "0":
            return  # Go back to main menu
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
