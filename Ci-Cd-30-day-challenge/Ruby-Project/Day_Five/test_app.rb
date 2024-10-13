require 'rspec'
require 'rack/test'
require_relative 'app'

RSpec.describe 'CRUD API' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it "creates a user" do
    post '/users', { name: 'John Doe', email: 'john@example.com' }.to_json
    expect(last_response.status).to eq(201)
  end

  it "gets all users" do
    get '/users'
    expect(last_response.status).to eq(200)
    expect(JSON.parse(last_response.body)).to be_an_instance_of(Array)
  end

  it "updates a user" do
    put '/users/1', { name: 'Updated Name' }.to_json
    expect(last_response.status).to eq(200)
  end

  it "deletes a user" do
    delete '/users/1'
    expect(last_response.status).to eq(204)
  end
end
