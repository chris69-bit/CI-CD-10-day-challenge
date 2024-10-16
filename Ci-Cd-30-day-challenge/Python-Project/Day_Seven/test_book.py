import pytest
from app import app, db, Book

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.create_all()  # Create tables before each test
    yield client
    with app.app_context():
        db.drop_all()  # Drop tables after each test

# Test CRUD: Create Book
def test_create_book(client):
    response = client.post('/books', json={
        'title': 'Test Book',
        'author': 'Author Name',
        'published_date': '2023-10-14'
    })
    assert response.status_code == 201
    assert response.json == {'message': 'Book created'}

# Test CRUD: Get Book by ID
def test_get_book(client):
    # Add a book to the database first
    book = Book(title='Sample Book', author='Author Name', published_date='2023-10-14')
    db.session.add(book)
    db.session.commit()

    response = client.get(f'/books/{book.id}')
    assert response.status_code == 200
    assert response.json == {
        'title': 'Sample Book',
        'author': 'Author Name',
        'published_date': '2023-10-14'
    }
