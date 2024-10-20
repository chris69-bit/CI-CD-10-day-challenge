require 'spec_helper'
require './app/models/book'

RSpec.describe Book, type: :model do
  it 'is valid with a title and author' do
    book = Book.new(title: 'Test Title', author: 'Test Author')
    expect(book).to be_valid
  end

  it 'is invalid without a title' do
    book = Book.new(title: nil)
    expect(book).not_to be_valid
  end

  it 'is invalid without an author' do
    book = Book.new(author: nil)
    expect(book).not_to be_valid
  end
end
