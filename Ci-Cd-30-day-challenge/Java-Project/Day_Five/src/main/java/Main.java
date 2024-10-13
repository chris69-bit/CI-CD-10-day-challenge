import controller.UserController;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        UserController controller = new UserController();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Choose an option: ");
        System.out.println("1. Create User");
        System.out.println("2. List Users");
        System.out.println("3. Update User");
        System.out.println("4. Delete User");

        int choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
            case 1:
                System.out.println("Enter name:");
                String name = scanner.nextLine();
                System.out.println("Enter email:");
                String email = scanner.nextLine();
                controller.createUser(name, email);
                break;
            case 2:
                controller.listUsers().forEach(user -> System.out.println(user.getName()));
                break;
            case 3:
                System.out.println("Enter user ID to update:");
                int idToUpdate = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Enter new name:");
                String newName = scanner.nextLine();
                System.out.println("Enter new email:");
                String newEmail = scanner.nextLine();
                controller.updateUser(idToUpdate, newName, newEmail);
                break;
            case 4:
                System.out.println("Enter user ID to delete:");
                int idToDelete = scanner.nextInt();
                controller.deleteUser(idToDelete);
                break;
            default:
                System.out.println("Invalid option.");
                break;
        }
    }
}
