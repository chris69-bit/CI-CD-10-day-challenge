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
