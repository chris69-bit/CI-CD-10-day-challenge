#Use the official runtime as the base image
FROM node:14-alpine

#Create a working directory inside the container
WORKDIR /app

#Copy the dependencies inside the container
COPY package.json /app
RUN npm install

#Copy the rest of the application
COPY . /app

#Expose port
EXPOSE 3000

#Run the application
CMD [ "npm", "start" ]