#Use official python runtime as the base image
FROM python-3.9-slim

#Create working directory inside the container
WORKDIR /usr/src/app

#Install system dependencies for sqlite
RUN apt-get update -qq && apt-get install -t sqlite3 libsqlite3-dev

#Install pyhton dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy the rest of the application
COPY . .

#Expose port number
EXPOSE 5000

#Set environment variable
ENV FLASK_APP=app.pyhton
ENV FLASK_ENV=development

#Command to run the application
CMD [ "flask", "run", "--host=0.0.0.0" ]
