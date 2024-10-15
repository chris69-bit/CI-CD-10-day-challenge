#Use official runtime as the base image
FROM ruby:3.0

#Create a working directory inside the container
WORKDIR /app

#Copy and install dependencies inside the containe
COPY Gemfile /app/
RUN bundle install

#Copy the rest of the application
COPY app.rb /app/

#Expose port
EXPOSE 5000

CMD [ "ruby", "app.rb" ]