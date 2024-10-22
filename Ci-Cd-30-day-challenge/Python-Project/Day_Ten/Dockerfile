#Use official python runtime as the base image
FROM python:3.9-slim

#Create a working directory inside the container
WORKDIR /app

#Install sqlite dependencies
RUN apt update -qq && apt install sqlite3 libsqlite3-dev

#Copy and install python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

#Copy the rest of the application
COPY . /app/

#Expose port 
EXPOSE 8080

#Run the application
CMD ["python3", ""]