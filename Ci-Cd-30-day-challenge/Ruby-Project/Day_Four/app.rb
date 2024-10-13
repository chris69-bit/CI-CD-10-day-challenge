require 'sinatra'

#get '/' do
#  'Hello, World!'
#end

#get '/hello/:name' do
#  "Hello, #{params[:name]}!"
#end

// SQLite integration
require 'sqlite3'

db = SQLite3::Database.new 'users.db'

db.execute <<-SQL
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
  );
SQL

# Create a new user
post '/users' do
  name = params[:name]
  email = params[:email]
  db.execute("INSERT INTO users (name, email) VALUES (?, ?)", [name, email])
  "User created"
end

# Read users
get '/users' do
  users = db.execute("SELECT * FROM users")
  users.to_json
end

# Update a user
put '/users/:id' do
  id = params[:id]
  name = params[:name]
  email = params[:email]
  db.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", [name, email, id])
  "User updated"
end

# Delete a user
delete '/users/:id' do
  id = params[:id]
  db.execute("DELETE FROM users WHERE id = ?", [id])
  "User deleted"
end
