#Use the official golang runtime as the base image
FROM golang:1.20

#Create a working directory
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq && apt-get install -y sqlite3 libsqlite3-dev

#Copy and install dependencies
COPY . /app/
RUN go build -o main 

#Expose port
EXPOSE 5000

#Run the application
CMD [ "./main" ]