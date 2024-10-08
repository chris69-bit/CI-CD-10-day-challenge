require 'minitest/autorun'
require_relative './app'

class AppTest < Minitest::Test
  def test_hello_name
    assert_equal 'Hello, Jenkins!', "Hello, Jenkins!"
  end
end

