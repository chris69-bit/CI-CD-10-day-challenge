import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/users', json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_update_user(client):
    response = client.put('/users/1', json={'name': 'John Updated', 'email': 'john.updated@example.com'})
    assert response.status_code == 200

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
