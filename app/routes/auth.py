from fastapi import APIRouter, Depends, HTTPException 
from app.services import auth_service 

router = APIRouter()

@router.post("/login", response_model=str) 
async def login(username: str, password: str, session=Depends(get_session)): 
  return await auth_service.login(username, password, session) 
  
@router.post("/logout") 
async def logout(): 
  return {"message": "Logged out"}
