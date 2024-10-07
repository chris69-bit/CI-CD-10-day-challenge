package main

import "testing"

func TestHelloWorld(t *testing.T) {
    expected := "Hello, World!"
    got := HelloWorld()
    if got != expected {
        t.Errorf("Expected %s, but got %s", expected, got)
    }
}
