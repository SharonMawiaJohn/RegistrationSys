from sqlalchemy import (Column, String, Integer, ForeignKey)
from models.models import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer(), primary_key = True)
    amount = Column(Integer())
    transaction_type = Column(String())
    timestamp = Column(String())
    acc_id = Column(Integer(), ForeignKey('accounts.id'))
    
    def __repr__(self):
        return f'Transaction(id={self.id}, ' + \
            f'amount={self.amount}, ' + \
            f'transaction_type={self.transaction_type}, ' + \
            f'timestamp={self.timestamp}, ' + \
            f'acc_id={self.acc_id})'