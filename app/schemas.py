from pydantic import BaseModel

class BookSchema(BaseModel):
  title: str 
  description: str
  publication_date: str 
  authors: list[str] 
  genres: list[str] 
  available_copies: int
  
class AuthorSchema(BaseModel): 
  name: str
  biography: str 
  date_of_birth: str 
  
class ReaderSchema(BaseModel): 
  name: str 
  email: str
