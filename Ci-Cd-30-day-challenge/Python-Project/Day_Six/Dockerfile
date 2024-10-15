#use an official runtime as the base image
FROM python:3.9-slim

#Create working directory inside the container
WORKDIR /app

#Copy contents to container
COPY . /app/
RUN pip install -r requirements.txt

#Expose port number
EXPOSE 8080

ENV FLASK_APP=app.py

CMD [ "flask", "run", "--host=0.0.0.0" ]