
from models.__init__ import init_db

if __name__ == '__main__':
    init_db()
    print("Database initialized.")
    import ipdb; ipdb.set_trace()