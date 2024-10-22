from flask import jsonify, request
from app import app, db
from app.models.book import Book

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_date=data['published_date'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created'}), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({'title': book.title, 'author': book.author, 'published_date': book.published_date})
