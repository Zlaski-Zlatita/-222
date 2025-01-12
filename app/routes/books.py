from fastapi import APIRouter, Depends, HTTPException 
from app.services import book_service 
from app.schemas import BookSchema

router = APIRouter()

@router.get("/books", response_model=list[BookSchema]) 
async def get_books(): 
  return await book_service.get_books() 
  
@router.post("/books", response_model=BookSchema) 
async def create_book(book: BookSchema, session=Depends(get_session)): 
  return await book_service.create_book(book, session)

@router.get("/books/{book_id}", response_model=BookSchema) 
async def get_book(book_id: int, session=Depends(get_session)): 
  book = await book_service.get_book(book_id, session) 
  if book is None: 
    raise HTTPException(status_code=404, detail="Book not found") 
  return book
