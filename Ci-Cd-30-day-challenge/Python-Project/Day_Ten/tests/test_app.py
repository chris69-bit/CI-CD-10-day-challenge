import pytest
from app import app, db
from app.models.book import Book

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_book(client):
    response = client.post('/books', json={
        'title': 'Test Book',
        'author': 'Author Name',
        'published_date': '2024-10-14'
    })
    assert response.status_code == 201

def test_get_book(client):
    book = Book(title='Sample Book', author='Author Name', published_date='2024-10-14')
    db.session.add(book)
    db.session.commit()
    response = client.get(f'/books/{book.id}')
    assert response.json['title'] == 'Sample Book'
