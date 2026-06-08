stored_username = "Simran2907"
stored_password = "@simran2907"
is_active = True

username = input("Username: ")
password = input("Password: ")

if username == stored_username:
    if is_active:
        if password == stored_password:
            print("Login Successful")
        else:
            print("Incorrect Password")
    else:
        print("Account is Inactive")
else:
    print("Username Not Found")