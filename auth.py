def login(username, password):
    if len(password) < 6:
        return "Password too short"
    return f"{username} logged in"
