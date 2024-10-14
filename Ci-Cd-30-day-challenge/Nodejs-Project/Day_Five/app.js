/*const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.get('/hello/:name', (req, res) => {
    res.send(`Hello, ${req.params.name}!`);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});*/

//Integrating SQLite

const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

const db = new sqlite3.Database('users.db');

// Create table
db.run('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)');

// Create a new user
app.post('/users', (req, res) => {
  const { name, email } = req.body;
  db.run('INSERT INTO users (name, email) VALUES (?, ?)', [name, email], () => {
    res.send('User created');
  });
});

// Read all users
app.get('/users', (req, res) => {
  db.all('SELECT * FROM users', (err, rows) => {
    res.json(rows);
  });
});

// Update user
app.put('/users/:id', (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;
  db.run('UPDATE users SET name = ?, email = ? WHERE id = ?', [name, email, id], () => {
    res.send('User updated');
  });
});

// Delete user
app.delete('/users/:id', (req, res) => {
  const { id } = req.params;
  db.run('DELETE FROM users WHERE id = ?', [id], () => {
    res.send('User deleted');
  });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
