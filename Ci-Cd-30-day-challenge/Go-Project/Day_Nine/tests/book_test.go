package tests

import (
	"go_project/api/controllers"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestCreateBook(t *testing.T) {
	req, err := http.NewRequest("POST", "/books", strings.NewReader(`{"title":"Test Book", "author":"Author", "published_date":"2024-10-14"}`))
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(controllers.CreateBook)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusCreated {
		t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusCreated)
	}
}

func TestGetBook(t *testing.T) {
	req
