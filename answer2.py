menu ="""
------------------------------------
|**********************************|
|    welcome to my_Ekuke bank.come |
|**********************************|   
|    please selet option           |
|**********************************|   
|    login to "login"              |
|**********************************|
|    register to "register"        |
|********************************* |  
|    exit to "exit"                |
|********************************* |
------------------------------------
"""
print(menu)

verivication_fee = 1500

database = {
        "israel": {
            "username": "israel", 
            "password": "9925",
            "Deposited_bal": 2000,
            "is_verified": True
            }

        }
choice = input("selet command" ).lower().strip()
if choice  not in ["login", "register", "exit"]:
    print("invalid option")

elif choice == "register":
    print("fill in the form below to login your account")
    username = input("create username").lower().strip()
    print(" ")
    if username in user_db:
        print(f"username {username} already taken")
    else:
        password = input("create your password: ")
        print(" ")
        initial_amount = float(input("Deposit amout: "))
        #is_verified = False
        database[username]= {
            "username": username,
            "password": password,
            "initial_amount": initial_amount,
            "is_verified": False

        }
        print("account created successfully")
        print(" ")
        print(f"welcome {username}")
        print(" ")
        verification = input("did you want verifie your account?: ").lower().strip()
        if verification == "yes" or "y":
            if initial_amount > verification_fee:
                initial_amount -= verfication_fee
                database.update({"is_verified": True})
                database.update({"initial_amount": initial_amount})
                print("account verified succssefuylly")
            else:
                print("insufficient balance")

            
