# brute-force login simulator

correct_username = "admin"
correct_password = "P@ssw0rd"

with open("passwords.txt", "r") as file:
    password_list = file.read().splitlines()

for attempt in password_list:
    print(f"Password attempt: {attempt}")

    if attempt == correct_password:
        print("Logged in successfully!")
        print(f"Username: {correct_username}, Password: {attempt}")
        break
else:
    print("Could not find the correct password.")