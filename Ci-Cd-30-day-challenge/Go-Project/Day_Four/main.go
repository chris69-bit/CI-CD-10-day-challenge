package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"
	"os"

    _ "github.com/mattn/go-sqlite3"
)

// Hello world 
/*func main() {
    if len(os.Args) > 1 {
        fmt.Println("Hello, " + os.Args[1] + "!")
    } else {
        fmt.Println("Hello, World!")
    }
}*/

var db *sql.DB

// Initialize the database
func initDB() {
    var err error
    db, err = sql.Open("sqlite3", "./users.db")
    if err != nil {
        log.Fatal(err)
    }

    // Create a users table
    _, err = db.Exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    if err != nil {
        log.Fatal(err)
    }
}

// Create a new user
func createUserHandler(w http.ResponseWriter, r *http.Request) {
    name := r.FormValue("name")
    email := r.FormValue("email")

    statement, _ := db.Prepare("INSERT INTO users (name, email) VALUES (?, ?)")
    statement.Exec(name, email)

    fmt.Fprintf(w, "New user created: %s (%s)", name, email)
}

// Read all users
func getUsersHandler(w http.ResponseWriter, r *http.Request) {
    rows, _ := db.Query("SELECT id, name, email FROM users")
    var users []string
    for rows.Next() {
        var id int
        var name, email string
        rows.Scan(&id, &name, &email)
        users = append(users, fmt.Sprintf("ID: %d, Name: %s, Email: %s", id, name, email))
    }
    fmt.Fprintf(w, "Users: %v", users)
}

// Update user details
func updateUserHandler(w http.ResponseWriter, r *http.Request) {
    id := r.FormValue("id")
    name := r.FormValue("name")
    email := r.FormValue("email")

    statement, _ := db.Prepare("UPDATE users SET name=?, email=? WHERE id=?")
    statement.Exec(name, email, id)

    fmt.Fprintf(w, "User updated: %s (%s)", name, email)
}

// Delete a user
func deleteUserHandler(w http.ResponseWriter, r *http.Request) {
    id := r.FormValue("id")

    statement, _ := db.Prepare("DELETE FROM users WHERE id=?")
    statement.Exec(id)

    fmt.Fprintf(w, "User with ID %s deleted", id)
}

// Register routes
func main() {
    initDB()

    // Route handlers for CRUD
    http.HandleFunc("/create", createUserHandler)
    http.HandleFunc("/users", getUsersHandler)
    http.HandleFunc("/update", updateUserHandler)
    http.HandleFunc("/delete", deleteUserHandler)

    log.Println("Starting server on :8080...")
    log.Fatal(http.ListenAndServe(":8080", nil))
}






