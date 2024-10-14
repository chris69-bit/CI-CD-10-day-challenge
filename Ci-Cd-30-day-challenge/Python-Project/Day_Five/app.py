from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)



# Initialize the database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return "User created", 201

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return jsonify(users)

# Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id))
    conn.commit()
    conn.close()
    return "User updated", 200

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return "User deleted", 200

if __name__ == '__main__':
    app.run(debug=True)
  