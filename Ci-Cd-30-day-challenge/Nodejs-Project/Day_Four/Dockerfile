#Use the official javascript runtime as the base image
FROM node:14-alpine

#Create a working directory inside the container
WORKDIR /app

#Copy all the files to the container
COPY . /app

#Install the dependencies
RUN npm Install

#Expose a port
EXPOSE 3000

#Run the application
CMD [ "node", "app.js" ]