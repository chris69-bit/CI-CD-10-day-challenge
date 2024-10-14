#Use official golang runtime as the  base image
FROM golang:1.17-alpine

#Create a working directory inside the container
WORKDIR /test_app

#Copy the rquired files inside the container
COPY main_test.go /test_app/
RUN go build -o main_test .

#Expose port
EXPOSE 8080

#Run the test
CMD [ "./main_test" ]