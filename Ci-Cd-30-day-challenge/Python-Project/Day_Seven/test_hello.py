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
