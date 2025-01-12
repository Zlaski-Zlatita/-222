from app.database import get_session 
from app.models import User 
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")
async def login(username: str, password: str, session):
  user = await get_session().query(User).filter_by(username=username).first() if not user or not pwd_context.verify(password, user.password): raise HTTPException(status_code=401, detail="Incorrect username or password") return user
