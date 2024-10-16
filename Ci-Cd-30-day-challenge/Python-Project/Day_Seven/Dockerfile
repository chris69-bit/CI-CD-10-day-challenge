#Use the official python runtime as the base image
FROM python:3.9-slim

#Create a working directory inside the container
WORKDIR /app

#Copy and install dependencies 
COPY requirements.txt /app
RUN pip install -r requirements.txt

#Copy the application
COPY app.py /app

#Expose port
EXPOSE 8080

#Run the application
CMD [ "python3", "app.py" ]