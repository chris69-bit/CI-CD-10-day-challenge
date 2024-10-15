from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite DB
def init_db():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

# HelloWorld endpoint
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

# CRUD: Create
@app.route('/item', methods=['POST'])
def create_item():
    name = request.json['name']
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify(message="Item created"), 201

# CRUD: Read
@app.route('/item', methods=['GET'])
def get_items():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    items = [{'id': row[0], 'name': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(items)

# Initialize the database when the app starts
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

