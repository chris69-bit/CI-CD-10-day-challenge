const request = require('supertest');
const app = require('./app'); // Ensure app is properly exported

describe('GET /hello', () => {
    it('should return Hello, World!', (done) => {
        request(app)
            .get('/hello')
            .expect('Hello, World!')
            .expect(200, done);
    });
});
