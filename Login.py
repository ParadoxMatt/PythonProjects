def menu():
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")
    return input(": ")
#Returns input for the choice for the menu option and takes the user there

def login():
    username = input("Enter your Username: ")
    userpass = input("Enter your password: ")

    with open("login.txt", "r") as file:
        data = file.read()

    if username in data and userpass in data:
        print("Login successful!")
    else:
        print("Invalid credentials")

def register():
    userRegister = input("Register your username: ")
    userpass = input("Register password: ")

    if not passkeytest(userpass):
        return

    with open("login.txt", "a") as file:  # Add name to the file with breaks 
        file.write(userRegister + "\n")
        file.write(userpass + "\n")

    print("You have successfully registered")


def passkeytest(password):
    symbols = ["!", "@", "#", "$", "&", "/","?","*","[","]"]

    if not any(sym in password for sym in symbols) and len(password) < 8:
        print("Your password must have at least one symbol and have 8 characters")
        return False
    if len(password) < 8:
        print("Password must have at least 8 characters")
        return False

    return True

def main():
    while True:
        option = menu()

        if option == "1":
            login()
        elif option == "2":
            register()
        elif option == "3":
            break
        else:
            print("Insert a valid option")

main()