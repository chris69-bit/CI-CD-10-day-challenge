const express = require('express');
const app = express();
const bookRoutes = require('./routes/bookRoutes');
const connectDB = require('./config/config');
require('dotenv').config();

// Middleware
app.use(express.json());
app.use('/api', bookRoutes);

// Connect to database
connectDB();

// Root route
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to the Book API!' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app;
