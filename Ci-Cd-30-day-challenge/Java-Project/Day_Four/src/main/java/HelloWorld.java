package main.java;

/*public class HelloWorld {
    public static void main(String[] args) {
        if (args.length > 0) {
            System.out.println("Hello, " + args[0] + "!");
        } else {
            System.out.println("Hello, World!");
        }
    }
}*/

// Initialize database
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DB {
    public static void init() {
        try {
            Connection connection = DriverManager.getConnection("jdbc:sqlite:users.db");
            Statement statement = connection.createStatement();
            String sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)";
            statement.execute(sql);
            statement.close();
            connection.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

//CRUD operations
import java.sql.*;

public class UserOperations {
    public static void createUser(String name, String email) {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:users.db")) {
            String query = "INSERT INTO users (name, email) VALUES (?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, email);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void getUsers() {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:users.db")) {
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM users");

            while (resultSet.next()) {
                System.out.println("ID: " + resultSet.getInt("id"));
                System.out.println("Name: " + resultSet.getString("name"));
                System.out.println("Email: " + resultSet.getString("email"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void updateUser(int id, String name, String email) {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:users.db")) {
            String query = "UPDATE users SET name=?, email=? WHERE id=?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, email);
            preparedStatement.setInt(3, id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void deleteUser(int id) {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:users.db")) {
            String query = "DELETE FROM users WHERE id=?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setInt(1, id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
