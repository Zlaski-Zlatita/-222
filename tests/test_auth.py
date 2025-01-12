import pytest
from app.services import auth_service 

def test_login():
  username = "test" password = "test"
  session = get_session()
  user = auth_service.login(username, password, session) 
  assert user.username == "test"
  
def test_logout(): 
  result = auth_service.logout() 
  assert result["message"] == "Logged out"
