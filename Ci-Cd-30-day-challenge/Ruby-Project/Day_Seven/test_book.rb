require 'minitest/autorun'
require 'rack/test'
require './app'

class BookTest < Minitest::Test
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def test_create_book
    post '/books', { title: 'Book Title', author: 'Author Name', published_date: '2023-10-14' }
    assert last_response.ok?
  end
end
