#Use official Maven runtime as the base image
FROM maven:3.8.4-openjdk-11-slim As build

#Create a working directory inside the container
WORKDIR /app

#Copy the pom.xml and install dependecies
COPY pom.xml /app
RUN mvn dependecies:go-offline

#Copy the rest of the application
COPY /src /app
RUN mvn package

#Run the built application in a smaller JDK image
FROM openjdk:11-jre-slim
COPY --from=build /app/target/myapp.jar /app/myapp.jar
ENTRYPOINT [ "java", "-jar", "/app/myapp.jar" ]