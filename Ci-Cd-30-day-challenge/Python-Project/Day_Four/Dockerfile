#Use official python runtime as the base image
FROM python:3.9-slim

#Create a working directory inside the container
WORKDIR /app

#Copy files inside the container
COPY . /app

#Install dependencies
RUN pip install -r requirements.txt

#Expose a port number
EXPOSE 8080

#Run the application
CMD [ "python3", "app.py" ]