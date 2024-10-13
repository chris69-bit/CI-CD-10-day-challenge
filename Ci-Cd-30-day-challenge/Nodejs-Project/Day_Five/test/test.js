const request = require('supertest');
const app = require('../app');
const expect = require('chai').expect;

describe('CRUD API', function() {
  it('should create a user', function(done) {
    request(app)
      .post('/users')
      .send({name: 'John Doe', email: 'john@example.com'})
      .expect(201, done);
  });

  it('should get all users', function(done) {
    request(app)
      .get('/users')
      .expect(200)
      .end(function(err, res) {
        expect(res.body).to.be.an('array');
        done();
      });
  });

  it('should update a user', function(done) {
    request(app)
      .put('/users/1')
      .send({name: 'Updated Name'})
      .expect(200, done);
  });

  it('should delete a user', function(done) {
    request(app)
      .delete('/users/1')
      .expect(204, done);
  });
});
