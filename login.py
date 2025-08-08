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

