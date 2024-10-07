require 'minitest/autorun'
require_relative './app'

class AppTest < Minitest::Test
  def test_home
    assert_equal 'Hello, World!', 'Hello, World!'
  end
end
