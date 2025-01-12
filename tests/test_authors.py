import pytest 
from app.models import Author
from app.services import author_service 

@pytest.fixture 
def author(): 
  return Author(name="Test author", biography="Test biography")
  
def test_get_authors():
  authors = author_service.get_authors() 
  assert len(authors) > 0
  
def test_create_author(author):
  author_service.create_author(author) 
  author = author_service.get_author(author.id) 
  assert author.name == "Test author" 
  
def test_get_author(author):
  author_service.create_author(author) 
  author = author_service.get_author(author.id) 
  assert author.name == "Test author"
