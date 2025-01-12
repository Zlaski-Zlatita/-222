from sqlalchemy import Column, Integer, String, DateTime, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship 

Base = declarative_base() 

class Book(Base): 
  __tablename__ = "books" 
  id = Column(Integer, primary_key=True) 
  title = Column(String) 
  description = Column(String) 
  publication_date = Column(DateTime)
  authors = relationship("Author", backref="books") genres = Column(String)
  available_copies = Column(Integer)
  
class Author(Base):
  __tablename__ = "authors" 
  id = Column(Integer, primary_key=True)
  name = Column(String)
  biography = Column(String)
  date_of_birth = Column(DateTime)
  
class Reader(Base):
  __tablename__ = "readers"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)
  
class Borrow(Base):
  __tablename__ = "borrows"
  id = Column(Integer, primary_key=True)
  reader_id = Column(Integer, ForeignKey("readers.id"))
  book_id = Column(Integer, ForeignKey("books.id"))
  borrowed_date = Column(DateTime)
  return_date = Column(DateTime)
