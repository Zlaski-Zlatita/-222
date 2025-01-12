import pytest 
from app.models import Reader
from app.services import reader_service

@pytest.fixture def reader():
  return Reader(name="Test reader", email="test@example.com") 

def test_get_readers(): 
  readers = reader_service.get_readers() 
  assert len(readers) > 0 
  
def test_create_reader(reader): 
  reader_service.create_reader(reader) 
  reader = reader_service.get_reader(reader.id)
  assert reader.name == "Test reader"
  
def test_get_reader(reader): 
  reader_service.create_reader(reader) 
  reader = reader_service.get_reader(reader.id)
  assert reader.name == "Test reader"
