menu = """
------------------------------------
|**********************************|
|    Welcome to my_Ekuke bank.com |
|**********************************|   
|    Please select an option       |
|**********************************|   
|    Login    → "login"            |
|**********************************|
|    Register → "register"         |
|**********************************|  
|    Exit     → "exit"             |
|**********************************|
------------------------------------
"""
print(menu)

verification_fee = 1500

user_db = {
    "israel": {
        "username": "israel", 
        "password": "9925",
        "Deposited_bal": 2000,
        "is_verified": True
    }
}

choice = input("Select command: ").lower().strip()

if choice not in ["login", "register", "exit"]:
    print("Invalid option")

elif choice == "register":
    print("Fill in the form below to create your account:")
    username = input("Create username: ").lower().strip()
    print(" ")
    
    if username in user_db:
        print(f"Username '{username}' is already taken.")
    else:
        password = input("Create your password: ")
        print(" ")
        initial_amount = float(input("Deposit amount: "))
        
        user_db[username] = {
            "username": username,
            "password": password,
            "Deposited_bal": initial_amount,
            "is_verified": False
        }
        
        print("Account created successfully.")
        print(f"Welcome, {username}!")
        print(" ")
        
        verification = input("Do you want to verify your account? (yes/no): ").lower().strip()
        
        if verification in ["yes", "y"]:
            if initial_amount > verification_fee:
                user_db[username]["Deposited_bal"] -= verification_fee
                user_db[username]["is_verified"] = True
                print("Account verified successfully.")
            else:
                print("Insufficient funds to verify account.")
        else:
            print("Account not verified.")

# ==================== SAMPLE DATABASE ====================
user_db = {
    "israelitegamer": {
        "username": "israelitegamer",
        "password": "1234",
        "Deposited_bal": 5000,
        "is_verified": True
    },
    "player2": {
        "username": "player2",
        "password": "abcd",
        "Deposited_bal": 2500,
        "is_verified": False
    }
}


# ==================== LOGIN ====================
print("\nLogin to your account:")
username = input("Username: ").lower().strip()
password = input("Password: ")

if username in user_db and user_db[username]["password"] == password:
    print(f"\nLogin successful. Welcome back, {username}!")
    user = user_db[username]

    print("\nACCOUNT DETAILS")
    print(f"Username : {user['username']}")
    print(f"Balance  : ₦{user['Deposited_bal']}")
    print(f"Verified : {'Yes' if user['is_verified'] else 'No'}")
else:
    print("Invalid username or password.")

