func TestCreateUser(t *testing.T) {
    request, _ := http.NewRequest("POST", "/users", nil)
    response := executeRequest(request)
    checkResponseCode(t, http.StatusCreated, response.Code)
}

