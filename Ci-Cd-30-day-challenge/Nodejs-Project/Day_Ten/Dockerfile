#Use official ruby runtime as the base image
FROM node:14-alpine

#Create a working directory inside the container
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq && apt-get install sqlite3 libsqlite3-dev

#Copy and install the apps dependecies 
COPY package.json /app/
RUN npm install

#Copy the rest of the apppication
COPY . /app/

#Expose port
EXPOSE 5000

#Run the application
CMD [ "npm", "start" ]