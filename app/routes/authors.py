from fastapi import APIRouter, Depends, HTTPException
from app.services import author_service

router = APIRouter()

@router.get("/authors", response_model=list[Author]) 
async def get_authors(): 
  return await author_service.get_authors() 
  
@router.post("/authors", response_model=Author) 
async def create_author(author: Author): 
  return await author_service.create_author(author)
