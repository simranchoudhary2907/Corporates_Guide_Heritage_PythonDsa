stored_username = "Simran2907"
stored_password = "@simran2907"

username = "Simran2907"
password = "@simran2907"
is_active = True

if username != stored_username:
    print("Username not found.")
elif password != stored_password:
    print("Incorrect password.")
elif not is_active:
    print("Account is deactivated.")
else:
    print(f"Login successful! Welcome, {username}.")