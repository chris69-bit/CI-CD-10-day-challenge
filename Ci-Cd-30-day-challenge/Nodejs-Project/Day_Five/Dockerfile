#Use offical node runtime as the base image
FROM node:14-alpine

#Create a working directory inside the container
WORKDIR  /app_test

#Copy dependencies and install
COPY package.json test/test.js /app_test/
RUN npm install

#Expose port
EXPOSE 3000

#Run the test
CMD [ "node", "test" ]