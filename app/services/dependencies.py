from fastapi.security import OAuth2PasswordBearer, 
OAuth2PasswordRequestForm

auth_scheme = OAuth2PasswordBearer(token_url="login") 

async def get_current_user(token: str = Depends(auth_scheme)):
  return(await 
       get_session().query(User).filter_by(username/token).first())
