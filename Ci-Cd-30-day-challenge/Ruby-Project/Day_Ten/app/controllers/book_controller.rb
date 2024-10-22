require 'sinatra'
require 'sinatra/activerecord'
require './app/models/book'

# Create Book
post '/books' do
  book = Book.new(params)
  if book.save
    status 201
    body "Book created"
  else
    status 400
    body "Error creating book"
  end
end

# Get Book by ID
get '/books/:id' do
  book = Book.find_by(id: params[:id])
  if book
    book.to_json
  else
    status 404
    body "Book not found"
  end
end

# Get all Books
get '/books' do
  books = Book.all
  books.to_json
end

# Delete Book
delete '/books/:id' do
  book = Book.find_by(id: params[:id])
  if book
    book.destroy
    status 200
    body "Book deleted"
  else
    status 404
    body "Book not found"
  end
end
