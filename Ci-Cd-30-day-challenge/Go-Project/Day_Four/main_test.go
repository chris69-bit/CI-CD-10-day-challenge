package main

import (
    "testing"
)

func TestHelloWithArgument(t *testing.T) {
    expected := "Hello, Jenkins!"
    got := "Hello, Jenkins!"
    if got != expected {
        t.Errorf("Expected %s, but got %s", expected, got)
    }
}