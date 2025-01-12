from app.database import get_session
from app.models import Book 

async def get_books(session): 
  return await session.query(Book).all() 

async def create_book(book, session):
  session.add(book) 
  await session.commit() 
  return book 
  
async def get_book(book_id, session):
  return await session.query(Book).get(book_id)
