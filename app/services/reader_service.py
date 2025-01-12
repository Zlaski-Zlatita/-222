from app.database import get_session 
from app.models import Reader 

async def get_readers(session): 
  return await session.query(Reader).all() 
  
async def create_reader(reader, session): 
  session.add(reader) 
  await session.commit()
  return reader
