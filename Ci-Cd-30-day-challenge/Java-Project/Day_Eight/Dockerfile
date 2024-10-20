#Use official maven runtime as the base image
FROM maven:3.8.1-openjdk-11 As build

#Create working directory
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq && apt-get install -y sqlite3 libsqlite3-dev

#Copy and install dependencies
COPY pom.xml /app/
RUN mvn dependency:go-offline

#Copy the rest of the application
COPY . .

#Package the application
RUN mvn package

#Set the built jar file for running
FROM openjdk:11-jre-slim
COPY --from=build /app/target/myapp.jar /app/myapp.jar

#Expose port
EXPOSE 8080

CMD [ "java", "-jar", "myapp.jar" ]
