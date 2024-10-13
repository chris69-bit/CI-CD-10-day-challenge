#Use official golang runtime as the base image
FROM golang:1.17-alpine

#Create working directory inside the container
WORKDIR /app

#Copy contants of current directory inside the container
COPY . .

#Build the application inside the container
RUN go build -o goapp main.go

#Expose port
EXPOSE 8080

#Run the application
CMD [ "./goapp" ]