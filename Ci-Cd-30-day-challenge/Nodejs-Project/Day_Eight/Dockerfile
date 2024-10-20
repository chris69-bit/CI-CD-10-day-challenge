#Use official node runtime as the base image
FROM node:20-slim

#Create a working directoryb inside the container
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq && apt-get install sqlite3 libsqlite3-dev

#Copy and install dependencies
COPY package.json /app/
RUN npm install

#Copy the rest of the application
COPY . .

#Expose port
EXPOSE 8080

#Run the application
CMD [ "npm", "start" ]