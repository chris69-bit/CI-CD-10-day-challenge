package main

import (
	"go_project/api/routes"
	"log"
	"net/http"
)

func main() {
	router := routes.SetupRouter() // Setting up routes
	log.Fatal(http.ListenAndServe(":8080", router))
}
