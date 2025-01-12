from app.database import get_session
from app.models import Author 

async def get_authors(session):
  return await session.query(Author).all() 
 
async def create_author(author, session):
  session.add(author)
  await session.commit() 
  return author
