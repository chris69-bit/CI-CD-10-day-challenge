#Use an official sinatra as the base image
FROM ruby:3.0

#Create working directory inside the container
WORKDIR /app_test

#Copy the dependencies inside the container
COPY test_app.rb Gemfile /app_test
RUN bundle install

#Expose port number
EXPOSE 8123

#Run the test 
CMD ["ruby", "test_app.rb"]
