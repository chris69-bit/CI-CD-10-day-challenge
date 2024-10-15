package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"
    _ "github.com/mattn/go-sqlite3"
)

func helloWorld(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World!")
}

func initDB() {
    db, err := sql.Open("sqlite3", "./items.db")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    statement, err := db.Prepare("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)")
    if err != nil {
        log.Fatal(err)
    }
    statement.Exec()
}

func main() {
    initDB()

    http.HandleFunc("/hello", helloWorld)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
