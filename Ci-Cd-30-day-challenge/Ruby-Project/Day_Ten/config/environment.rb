require 'sinatra'
require 'sinatra/activerecord'
require './app/models/book'

# Database configuration
set :database, {adapter: "sqlite3", database: "db/development.sqlite3"}
