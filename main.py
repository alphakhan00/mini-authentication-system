


from datetime import datetime

current_user = None


def write_log(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a") as file:
        file.write(f"{time} - {message}\n")



def register():
    username = input("Enter username: ")

    if username.strip() == "":
        print("Username cannot be empty")
        return
    
    if len(username) < 6 or len(username) > 12:
        print("Username must be between 6 and 12 characters")
        return

    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password != confirm_password:
        print("Passwords do not match")
        return

    letters = 0
    numbers = 0

    for char in password:
        if char.isalpha():
            letters += 1

        elif char.isdigit():
            numbers += 1

    if letters < 3 or numbers < 5:
        print("Password must contain at least 3 letters and 5 numbers")
        return

    # check if file exists and read users
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        users = []

    # check duplicate username
    for user in users:
        stored_username, stored_password = user.strip().split(",")

        if username == stored_username:
            print("Username already exists! Try another one.")
            return

    # save new user
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("User registered successfully!")
    
    write_log(f"{username} registered")


def login():
    global current_user

    if current_user:
        print("A user is already logged in.")
        print("Please logout first.")
        return

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No users registered yet.")
        return

    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and password == stored_password:
                print("Login successful!")
                current_user = username
                write_log(f"{username} logged in")
                return

        attempts += 1
        print(f"Invalid username or password! Attempts left: {3 - attempts}")

    print("Too many failed attempts. Login blocked for this session.")



def logout():
    global current_user

    if current_user:
        print(f"{current_user} logged out")
        write_log(f"{current_user} logged out")
        current_user = None
    else:
        print("No user is currently logged in")



def view_logs():
    try:
        with open("log.txt", "r") as file:
            logs = file.read()

        if logs:
            print("\n===== ACTIVITY LOGS =====")
            print(logs)
        else:
            print("No logs available.")

    except FileNotFoundError:
        print("Log file does not exist yet.")


def show_current_user():
    global current_user

    if current_user:
        print(f"Current User: {current_user}")
    else:
        print("No user is logged in")



while True:
    print("\n===== LOGIN SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. View Logs")
    print("4. Logout")
    print("5. Show Current User")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()
    
    elif choice == "3":
        view_logs()

    elif choice == "4":
        logout()

    elif choice == "5":
        show_current_user()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")
