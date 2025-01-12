import pytest
from app.models import Book
from app.services import book_service

@pytest.fixture 
def book(): 
  return Book(title="Test book", description="Test description")
  
def test_get_books(): 
  books = book_service.get_books() 
  assert len(books) > 0
  
def test_create_book(book): 
  book_service.create_book(book) 
  book = book_service.get_book(book.id) 
  assert book.title == "Test book" 
  
def test_get_book(book): 
  book_service.create_book(book) 
  book = book_service.get_book(book.id) 
  assert book.title == "Test book"
