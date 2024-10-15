const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const port = 3000;

// Create SQLite database
let db = new sqlite3.Database('./items.db', (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the SQLite database.');
});

// Create items table
db.run('CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name TEXT)');

app.get('/hello', (req, res) => {
    res.send('Hello, World!');
});

app.listen(port, () => {
    console.log(`App running on port ${port}`);
});
