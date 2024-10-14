import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/users', data={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200

