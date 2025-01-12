from sqlalchemy import create_engine
from app.models import Book, Author, Reader, Borrow 
from sqlalchemy.orm import sessionmaker 

engine = create_engine("postgresql://user:password@localhost/database") 
Session = sessionmaker(bind=engine) 

def get_session():
  return Session()
