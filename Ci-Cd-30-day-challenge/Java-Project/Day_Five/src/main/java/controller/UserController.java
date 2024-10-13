package controller;

import service.UserService;
import model.User;

import java.util.List;

public class UserController {
    private final UserService userService = new UserService();

    public void createUser(String name, String email) {
        User user = new User(0, name, email);
        userService.addUser(user);
        System.out.println("User created: " + name);
    }

    public List<User> listUsers() {
        return userService.getAllUsers();
    }

    public void updateUser(int id, String name, String email) {
        User user = new User(id, name, email);
        userService.updateUser(id, user);
        System.out.println("User updated: " + name);
    }

    public void deleteUser(int id) {
        userService.deleteUser(id);
        System.out.println("User deleted with id: " + id);
    }
}

