#Use the official runtime as the base image
FROM ruby:3.0

#Create a working directory
WORKDIR /app

#Copy and install dependencies
COPY Gemfile /app/
RUN bundle install

#Copy the rest of the files
COPY  app.rb /app/

#Expose port
EXPOSE 5000

CMD [ "ruby", "app.rb" ]