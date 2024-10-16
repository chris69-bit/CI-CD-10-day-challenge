from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Item model for the 'items' table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# Define the Book model for the 'books' table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.String(100))

# HelloWorld endpoint
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

# CRUD: Create Item
@app.route('/item', methods=['POST'])
def create_item():
    name = request.json['name']
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(message="Item created"), 201

# CRUD: Get Items
@app.route('/item', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

# CRUD: Create Book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_date=data['published_date'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created'}), 201

# CRUD: Get Book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({'title': book.title, 'author': book.author, 'published_date': book.published_date})

# Initialize the database when the app starts
if __name__ == '__main__':
    app.run(debug=True)

