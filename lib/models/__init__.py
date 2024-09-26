from .account import Account
from .customer import Customer
from .transaction import Transaction
from .loan import Loan

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = 'sqlite:///bank.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(bind=engine)
