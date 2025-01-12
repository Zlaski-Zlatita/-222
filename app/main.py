from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from app.routes import book_router, author_router, reader_router, auth_router 
from app.services import book_service, author_service, reader_service, auth_service 
from app.dependencies import auth_dependency 
from app.utils import logger 

app = FastAPI() 

origins = ["*"] 

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"], 
) 

app.include_router(book_router) 
app.include_router(author_router) 
app.include_router(reader_router) 
app.include_router(auth_router) 

@app.on_event("shutdown") 
async def shutdown_event(): 
  logger.info("Application is shutting down") 
  await auth_service.revoke_all_tokens()
