users = {
    "Hassan": "xyz@12",
    "Sameer": "xyz@123",
    "Hammad": "xyz@1234"
}

def signup():
    name = input("Enter your name: ")
    if name in users:
        print("Username already exists! Please choose a different name.")
        return
    password = input("Enter your password: ")
    users[name] = password
    print("Signup successful! You can now login.")

def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if users.get(name) == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
 