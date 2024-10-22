require 'sinatra/activerecord'
require 'rspec'
require 'rack/test'

ENV['RACK_ENV'] = 'test'

RSpec.configure do |config|
  config.after(:suite) do
    ActiveRecord::Base.subclasses.each(&:delete_all)
  end
end
