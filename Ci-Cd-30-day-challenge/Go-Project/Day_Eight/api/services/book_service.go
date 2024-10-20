package services

import (
	"go_project/api/models"
)

var books []models.Book

func CreateBook(book models.Book) {
	books = append(books, book)
}

func GetBookByID(id int) models.Book {
	for _, book := range books {
		if book.ID == id {
			return book
		}
	}
	return models.Book{}
}
