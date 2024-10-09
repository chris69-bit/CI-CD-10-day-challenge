package main.java;

import static org.junit.Assert.*;
import org.junit.Test;

public class HelloWorldTest {

    @Test
    public void testHelloWorld() {
        assertEquals("Hello, World!", "Hello, World!");
    }

    @Test
    public void testHelloWithName() {
        assertEquals("Hello, Jenkins!", "Hello, Jenkins!");
    }
}

