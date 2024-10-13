#Use Maven runtime for the build stage
FROM maven:3.8.1openjdk-11 As build

#Create a working directory inside the container
WORKDIR /testapp

#Copy and install dependencies
COPY . /testapp
RUN mvn dependency:go-offline

#Package the application
RUN mvn package

#Set the built jar file for running
FROM openjdk:11-jre-slim
COPY --from=build /testapp/target/myapp.jar /testapp/myapp.jar

ENTRYPOINT [ "java", "-jar", "myapp.jar" ]