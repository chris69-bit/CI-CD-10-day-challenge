import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

# Test HelloWorld route
def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

# Test CRUD: Create Item
def test_create_item(client):
    response = client.post('/item', json={"name": "test_item"})
    assert response.status_code == 201
    assert response.json == {"message": "Item created"}

# Test CRUD: Get Items
def test_get_items(client):
    response = client.get('/item')
    assert response.status_code == 200

