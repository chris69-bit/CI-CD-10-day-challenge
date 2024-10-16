require 'sinatra'
require 'sqlite3'

db = SQLite3::Database.new 'test.db'

# Create table if not exists
db.execute <<-SQL
  CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT
  );
SQL

get '/hello' do
  'Hello, World!'
end

post '/item' do
  db.execute "INSERT INTO items (name) VALUES (?)", [params[:name]]
  'Item created!'
end

get '/items' do
  db.execute( "SELECT * FROM items" ).to_json
end