const request = require('supertest');
const app = require('../app');
const mongoose = require('mongoose');
const Book = require('../models/book');

describe('Book API', () => {
    beforeAll(async () => {
        await mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });
    });

    afterEach(async () => {
        await Book.deleteMany();
    });

    afterAll(async () => {
        await mongoose.connection.close();
    });

    test('It should create a new book', async () => {
        const response = await request(app)
            .post('/books')
            .send({ title: 'Test Book', author: 'Author', publishedDate: '2023-10-14' });

        expect(response.statusCode).toBe(201);
        expect(response.body.book.title).toBe('Test Book');
    });

    test('It should get all books', async () => {
        const book = new Book({ title: 'Test Book', author: 'Author', publishedDate: '2023-10-14' });
        await book.save();

        const response = await request(app).get('/books');
        expect(response.statusCode).toBe(200);
        expect(response.body.length).toBe(1);
    });
});
