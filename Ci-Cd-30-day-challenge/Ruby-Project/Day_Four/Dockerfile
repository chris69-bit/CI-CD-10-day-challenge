#Use an official runtime as the base image
FROM ruby:3.0

#Create working directory inside the container
WORKDIR /app

#Copy contents of the host to the container
COPY . /app/

#Install dependencied
RUN bundle Install

#Expose port
EXPOSE 4567

#Run the application
CMD [ "ruby", "app.rb" ]