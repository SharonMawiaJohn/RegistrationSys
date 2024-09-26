from models.account import Account
from models.customer import Customer
from models.loan import Loan
from models.transaction import Transaction


def exit_program():
    print("Goodbye!")
    exit()

#customer methods
def create_customer(session):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    
    customer = Customer(name=name, email=email, phone=phone, address=address)
    save(session, customer)

def save(session, obj):
    session.add(obj)
    session.commit()

def update_customer(session):
    customer_id = input("Enter the customer's ID: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        try:
            # Prompt for new details
            name = input("Enter the new name: ")
            email = input("Enter the new email: ")
            phone = input("Enter the new phone: ")
            address = input("Enter the new address: ")
            
            # Update customer details
            customer.name = name
            customer.email = email
            customer.phone = phone
            customer.address = address

            # Save the updated customer
            save(session, customer)
            print(f'Success: {customer}')
        except Exception as exc:
            print("Error updating customer: ", exc)
    else:
        print(f'Customer with ID {customer_id} not found')

def delete_customer(session):
    customer_id = input("Enter the customer's ID that needs to be deleted: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        try:
            session.delete(customer)
            session.commit()
            print(f"Customer with ID {customer_id} has been deleted.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting customer: {e}")
    else:
        print(f'Customer with ID {customer_id} not found')

def list_customers(session):    
    try:        
        customers = session.query(Customer).all()
        print(f"Found {len(customers)} customers.")
        for customer in customers:
            print(f"Customer ID: {customer.id}, Name: {customer.name}")
        return customers
    except Exception as e:
        print(f"Error querying customers: {e}")
        return []

def find_customer_by_name(session):
    name = input("Enter the customer's name: ")
    customer = session.query(Customer).filter(Customer.name == name).first()
    if customer:
        print(customer)
    else:
        print("Customer not found.")

def find_customer_by_id(session):
    customer_id = input("Enter the customer's ID: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        print(customer)
    else:
        print("Customer not found.")

#account methods           
def create_account(session):
    acc_number = input("Enter account number: ")
    acc_type = input("Enter account type: ")
    balance = input("Enter account balance: ")
    customer_id = input("Enter customer id: ")

    account = Account(acc_number=acc_number, acc_type=acc_type, balance=balance, customer_id=customer_id)
    save(session, account)

def update_account(session):
    acc_id = input("Enter account ID: ")
    account = session.query(Account).filter(Account.id == acc_id).first()

    if account:
        try:
            acc_number = input("Enter the new account number: ")
            acc_type = input("Enter the new account type: ")
            balance = input("Enter the new balance: ")
            customer_id = input("Enter the new customer id: ")

            account.acc_number = acc_number
            account.acc_type = acc_type
            account.balance = balance
            account.customer_id = customer_id

            save(session, account)
            print(f'Success: {account}')
        except Exception as exc:
            print("Error updating account: ", exc)
    else:
        print(f'Account with ID {acc_id} not found')

def delete_account(session):
    acc_id = input("Enter account ID that needs to be deleted: ")
    account = session.query(Account).filter(Account.id == acc_id).first()

    if account:
        try:
            session.delete(account)
            session.commit()
            print(f"Account with ID {acc_id} has been deleted.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting account: {e}")
    else:
        print(f'Account with ID {acc_id} not found')


def list_accounts(session):
    try:        
        accounts = session.query(Account).all()
        print(f"Found {len(accounts)} accounts.")
        for account in accounts:
            print(f"Account ID: {account.id}, Account Number: {account.acc_number}, Account Type: {account.acc_type}, Balance: {account.balance}")
        return accounts
    except Exception as e:
        print(f"Error querying customers: {e}")
        return []

def find_account_by_number(session):
    acc_number = input("Enter account number: ")
    account = session.query(Account).filter(Account.acc_number == acc_number).first()
    if account:
        print(account)
    else:
        print("Account not found.")

def find_account_by_id(session):
    acc_id = input("Enter account ID: ")
    account = session.query(Account).filter(Account.id == acc_id).first()
    if account:
        print(account)
    else:
        print("Account not found.")

#transaction methods
def create_transaction(session):
    amount = input("Enter transaction amount: ")
    transaction_type = input("Enter transaction type: ")
    timestamp = input("Enter timestamp: ")
    acc_id = input("Enter account id: ")    
    
    transaction = Transaction(amount=amount, transaction_type=transaction_type, timestamp=timestamp, acc_id=acc_id)
    save(session, transaction)

def update_transaction(session):
    transaction_id = input("Enter transaction ID: ")
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction:
        try:
            #Prompt for new details
            amount = input("Enter transaction amount: ")
            transaction_type = input("Enter transaction type: ")
            timestamp = input("Enter timestamp: ")
            acc_id = input("Enter account id: ")

            #Update transaction details
            transaction.amount = amount
            transaction.transaction_type = transaction_type
            transaction.timestamp = timestamp
            transaction.acc_id = acc_id

            #Save updated transaction
            save(session, transaction)
            print(f'Success: {transaction}')
        except Exception as exc:
            print("Error updating transaction: ", exc)
    else:
        print(f'Transaction with ID {transaction_id} not found')

def delete_transaction(session):
    transaction_id = input("Enter transaction ID that needs to be deleted: ")
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()

    if transaction:
        try:
            session.delete(transaction)
            session.commit()
            print(f"Transaction with ID {transaction_id} has been deleted.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting transaction: {e}")
    else:
        print(f'Transaction with ID {transaction_id} not found')


def find_transaction_by_id(session):    
    transaction_id = input("Enter transaction ID: ")
    transaction = session.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        print(transaction)
    else:
        print("Transaction not found.")

#loan methods
def create_loan(session):
    loan_amount = input("Enter loan amount: ")
    interest_rate = input("Enter interest rate: ")
    due_date = input("Enter due date: ")
    customer_id = input("Enter customer id: ")
    
    loan = Loan(loan_amount=loan_amount, interest_rate=interest_rate, due_date=due_date, customer_id=customer_id)
    save(session, loan)

def update_loan(session):
    loan_id = input("Enter loan ID: ")
    loan = session.query(Loan).filter(Loan.id == loan_id).first()

    if loan:
        try:
            #Prompt for new details
            loan_amount = input("Enter loan amount: ")
            interest_rate = input("Enter interest rate: ")
            due_date = input("Enter due date: ")
            customer_id = input("Enter customer id: ")

            #Update loan details
            loan.loan_amount = loan_amount
            loan.interest_rate = interest_rate
            loan.due_date = due_date
            loan.customer_id = customer_id

            # Save the updated loan
            save(session, loan)
            print(f'Success: {loan}')
        except Exception as exc:
            print("Error updating loan: ", exc)
    else:
        print(f'Customer with ID {customer_id} not found')

def delete_loan(session):
    loan_id = input("Enter loan ID: ")
    loan = session.query(Loan).filter(Loan.id == loan_id).first()

    if loan:
        try:
            session.delete(loan)
            session.commit()
            print(f"Loan with ID {loan_id} has been deleted.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting loan: {e}")
    else:
        print(f'Loan with ID {loan_id} not found')

def find_loan_by_id(session):
    loan_id = input("Enter loan ID: ")
    loan = session.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        print(loan)
    else:
        print("Loan not found.")

#relationship methods
def list_customer_accounts(session):    
    try:        
        customer_id = input("Enter the customer's ID: ")
        customer_accounts = session.query(Account).filter(Account.customer_id == customer_id).all()
        print(f"Found {len(customer_accounts)} accounts for ID: {customer_id}.")
        for account in customer_accounts:
            print(f"Account belonging to Customer ID:{account.customer_id}, Account ID: {account.id}, Account Number: {account.acc_number}, Account Type: {account.acc_type}, Balance: {account.balance}")
        return customer_accounts
    except Exception as e:
        print(f"Error querying customer accounts: {e}")
        return []
    
def list_customer_loans(session):
    try:        
        customer_id = input("Enter the customer's ID: ")
        customer_loans = session.query(Loan).filter(Loan.customer_id == customer_id).all()
        print(f"Found {len(customer_loans)} loans for ID: {customer_id}.")
        for loan in customer_loans:
            print(f"Loans belonging to Customer ID:{loan.customer_id}, Loan ID: {loan.id}, Loan amount: {loan.loan_amount}, Interest rate: {loan.interest_rate}, Due date: {loan.due_date}")
        return customer_loans
    except Exception as e:
        print(f"Error querying customer loans: {e}")
        return []    

def list_account_transactions(session):
    try:        
        acc_id = input("Enter account ID: ")
        account_transactions = session.query(Transaction).filter(Transaction.acc_id == acc_id).all()
        print(f"Found {len(account_transactions)} transactions for ID: {acc_id}.")
        for transaction in account_transactions:
            print(f"Transactions belonging to Account ID:{transaction.acc_id}, Transaction ID: {transaction.id}, Transaction amount: {transaction.amount}, Transaction type: {transaction.transaction_type}, Timestamp: {transaction.timestamp} ")
        return account_transactions
    except Exception as e:
        print(f"Error querying account transactions: {e}")
        return []  