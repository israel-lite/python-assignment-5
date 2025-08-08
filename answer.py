menu ="""
|**************************************|
|        welcome to Ekuke bank.com     |
|______________________________________|
|    1. Enter "login" to login         |
|______________________________________|
|    2. Enter "register" to register   |
|______________________________________|

"""
print(menu)

database = {
        "ekuke": {
            "username": "ekuke",
            "password": "admin123",
            "initial_balance": 2000,
            "is_Verified": True
            }
        }
#print(database)

option = input("select command: ").lower().strip()

if option not in ["login", "register"]:
    print("Invalid command")

elif option == "register":
    print("kindly input your details to register your account...")
    username = input("Create Useraname: ").lower().strip()
    if username in database:
        print(f"username: {username}, already taken!")
    else:
        password = input("Create password: ")
        print("-------------------------------------------")
        initial_balance = float(input("Enter amount you wish to deposit: "))
        print("-------------------------------------------")
        is_Verified = False

