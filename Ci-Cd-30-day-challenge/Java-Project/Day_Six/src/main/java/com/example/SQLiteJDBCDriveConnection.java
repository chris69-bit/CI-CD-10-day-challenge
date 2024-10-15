package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class SQLiteJDBCDriverConnection {

    public void createTable() {
        String url = "jdbc:sqlite:sample.db";
        String sql = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)";

        try (Connection conn = DriverManager.getConnection(url);
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
            System.out.println("Table created successfully.");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

