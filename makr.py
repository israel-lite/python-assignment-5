    user_db = {"mark": {"password": 1234, "balance": 2000, "is_verified": False} }

    command = input("do you want to login or register::")
    command = command.lower()
if command == "login":
    username = input("Enter your username: ")
    if username in user_db:
        password = int(input("Enter your password: "))
        if password == user_db[username] ["password"]:
            print(f" welcome! {username} ")
            print(f" login sucessfull")
        else:
            print(f"invalid password {username} ")
        else:
            print(f"{username}
