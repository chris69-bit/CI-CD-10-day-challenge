package migrations

import (
	"database/sql"
	"fmt"
	"log"
)

func Migrate(db *sql.DB) {
	query := `CREATE TABLE IF NOT EXISTS books (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT,
		author TEXT,
		published_date TEXT
	);`

	_, err := db.Exec(query)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Migration complete!")
}
