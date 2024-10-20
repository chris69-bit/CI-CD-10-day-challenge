#Use official runtime as the base image
FROM ruby:3.0

#Create a working directory
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq && apt-get install sqlite3 libsqlite3-dev

#Copy and install application dependenvcies
COPY Gemfile /app/
RUN bundle install

#Copy the rest of the application
COPY . /app

#Expose port
EXPOSE 8080

#Run the application
CMD [ "bundle", "exec", "rackup", "--host", "0.0.0.0", "port", "8080" ]