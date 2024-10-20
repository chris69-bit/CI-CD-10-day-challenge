#Use official golang runtime as the base image
FROM golang:1.19 as builder

#Create workking directory inside the container
WORKDIR /app

#Copy go modules and install dependencies
COPY go.mod go.sum /app/
RUN go mod download

#Copy the rest of the application
COPY . /app/

#Build the go application
RUN go build -o myapp

#New container for runnning the application
FROM debian:bullseye-slim

# Install SQLite dependencies in the runtime container
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Copy the Go app binary from the builder stage
COPY --from=builder /app/myapp /usr/local/bin/myapp

# Expose port 8080 for the Go web service
EXPOSE 8080

# Command to run the Go application
CMD ["myapp"]