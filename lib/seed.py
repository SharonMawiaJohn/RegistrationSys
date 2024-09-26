from faker import Faker
import random

from models.__init__ import init_db, session

from models.account import Account
from models.customer import Customer
from models.transaction import Transaction
from models.loan import Loan


if __name__ == '__main__':
    init_db()    

    session.query(Account).delete()
    session.query(Customer).delete()
    session.query(Transaction).delete()
    session.query(Loan).delete()

    fake = Faker()

    # Generate seed data
    customers = []
    accounts = []
    transactions = []
    loans = []

    # Create fake customers
    for _ in range(10):  # Generating 10 customers
        customer = Customer(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(customer)
        session.flush()  # This ensures customer gets an ID before we add related records
        customers.append(customer)

        # Create 1-3 accounts for each customer
        for _ in range(random.randint(1, 3)):
            account = Account(
                acc_number=fake.random_number(digits=10),
                acc_type=random.choice(['savings', 'current']),
                balance=random.randint(1000, 10000),
                customer_id=customer.id
            )
            session.add(account)
            session.flush()
            accounts.append(account)

            # Create 1-5 transactions for each account
            for _ in range(random.randint(1, 5)):
                transaction = Transaction(
                    amount=random.randint(100, 5000),
                    transaction_type=random.choice(['deposit', 'withdrawal']),
                    timestamp=fake.date_time_this_year(),
                    acc_id=account.id
                )
                session.add(transaction)
                transactions.append(transaction)

        # Create 1-2 loans for each customer
        for _ in range(random.randint(1, 2)):
            loan = Loan(
                loan_amount=random.randint(5000, 20000),
                interest_rate=f'{random.uniform(5.0, 15.0):.2f}%',
                due_date=fake.future_date(),
                customer_id=customer.id
            )
            session.add(loan)
            loans.append(loan)

    # Commit all seed data to the database
    session.commit()

    print(f"Seeded {len(customers)} customers, {len(accounts)} accounts, {len(transactions)} transactions, and {len(loans)} loans.")
