from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

ENGINE = create_engine('sqlite:///honeypot_db.db')
BASE = declarative_base(bind=ENGINE)
SESSION = sessionmaker(bind=ENGINE)()

