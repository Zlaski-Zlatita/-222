from fastapi import APIRouter, Depends, HTTPException 
from app.services import reader_service 

router = APIRouter() 

@router.get("/readers", response_model=list[Reader]) 
async def get_readers(): 
  return await reader_service.get_readers()
  
@router.post("/readers", response_model=Reader) 
async def create_reader(reader: Reader): 
  return await reader_service.create_reader(reader)
