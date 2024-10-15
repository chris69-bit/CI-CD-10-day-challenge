#Use official runtime as the base image 
FROM golang:1.20

#Create working directory inside the container
WORKDIR /app

#Copy and install dependencies
COPY . /app/
RUN go build main.go

#Expose port 
EXPOSE 3000

#Run the application
CMD [ "./main" ]