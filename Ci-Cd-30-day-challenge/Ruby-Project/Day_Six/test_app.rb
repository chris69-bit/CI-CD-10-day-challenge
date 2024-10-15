require 'minitest/autorun'
require 'rack/test'
require './app'

class AppTest < Minitest::Test
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  def test_hello_world
    get '/hello'
    assert last_response.ok?
    assert_equal 'Hello, World!', last_response.body
  end
end
