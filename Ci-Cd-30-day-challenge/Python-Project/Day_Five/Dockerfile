#Use official python runtime as the base image 
FROM python:3.9-slim

#Create working directory inside the container
WORKDIR /app_test

#Copy dependencies and install
COPY test_app.py requirements.txt /app_test/
RUN pip install -r requirements.txt

#Expose port 
EXPOSE 8080

CMD [ "pytest" ]