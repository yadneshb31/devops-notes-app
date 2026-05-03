def login(username, password):
    if len(password) < 6:
        return "Password too short"
    
    if username == "admin" and password == "1234":
        return "Admin logged in"
    
    if password == "admin123":
        return "Welcome Admin"
    
    return f"{username} logged in"
