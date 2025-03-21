import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_post_data(client):
    response = client.post('/api/data', json={"name": "John"})
    assert response.status_code == 201
    assert b'Hello, John!' in response.data
