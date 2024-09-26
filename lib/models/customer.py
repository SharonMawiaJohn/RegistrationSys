from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship, backref
from models.models import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())

    loans = relationship('Loan', backref=backref('customer'))
    accounts = relationship('Account', backref=backref('customer'))
    
    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'email={self.email}, ' + \
            f'phone={self.phone}, ' + \
            f'address={self.address})'
    
    