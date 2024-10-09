#Use an official runtime as the base image
FROM golang:1.20

#Create a workind directory inside the container
WORKDIR /app

#Copy the contents of your current directory to the container's directory
COPY . /app

#Build the application
RUN go build -o main .

#Expose a port for the container
EXPOSE 8080

#Run the executable
CMD ["./main"]


