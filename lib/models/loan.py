from sqlalchemy import (Column, String, Integer, ForeignKey)
from models.models import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer(), primary_key = True)
    loan_amount = Column(Integer())
    interest_rate = Column(String())
    due_date = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'Loan(id={self.id}, ' + \
            f'loan_amount={self.loan_amount}, ' + \
            f'interest_rate={self.interest_rate}, ' + \
            f'due_date={self.due_date}, ' + \
            f'customer_id={self.customer_id})'
    