package controllers

import (
	"encoding/json"
	"go_project/api/models"
	"go_project/api/services"
	"net/http"
	"strconv"
	"github.com/gorilla/mux"
)

func CreateBook(w http.ResponseWriter, r *http.Request) {
	var book models.Book
	_ = json.NewDecoder(r.Body).Decode(&book)
	services.CreateBook(book)
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(book)
}

func GetBook(w http.ResponseWriter, r *http.Request) {
	id, _ := strconv.Atoi(mux.Vars(r)["id"])
	book := services.GetBookByID(id)
	json.NewEncoder(w).Encode(book)
}
