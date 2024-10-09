#Use official runtime as the base image
FROM maven:3.8.1-openjdk-11 AS build

#Set the working directory inside the container
WORKDIR /app

#Copy the pom and install dependencies
COPY pom.xml .
RUN mvn dependency:go-offline

#Copy the rest of the app and build it
COPY src ./src
RUN mvn package

#Run the built jar in smaller JDK image
FROM openjdk:11-jre-slim
COPY --from=build /app/target/myapp.jar /app/myapp.jar

ENTRYPOINT ["java", "-jar", "/app/myapp.jar"]
