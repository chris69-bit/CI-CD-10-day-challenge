#Use official ruby runtime as the base image
FROM ruby:3.0

#Update and install dependencies for packages
RUN apt-get update -qq && apt-get install -y build-essential libsqlite3-dev

#Set the working directory inside the container
WORKDIR /usr/src/app

#Copy inside the container
COPY Gemfile Gemfile.lock ./
RUN bundle install

#Copy the application
COPY . /usr/src/app/

#Expose running port
EXPOSE 4567

#Command to the application
CMD [ "bundle", "exec", "rackup", "--host", "0.0.0.0", "--port", "4567" ]

