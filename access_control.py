print("AI Security Lab - Access Control System")

import json
import hashlib
from datetime import datetime
from getpass import getpass


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


with open("Scripts/users.json", "r") as file:
    users_data = json.load(file)

print(users_data)

attempt = 1
failed_attempts = 0

while attempt <= 3:
    print("Login attempt:", attempt)

    username = input("Enter username: ")

    if username.strip() == "":
        print("Username cannot be empty.")
        continue

    password = getpass("Enter password: ")

    if password.strip() == "":
        print("Password cannot be empty.")
        continue

    hashed_password = hash_password(password)

    found_user = None

    for user in users_data["users"]:
        if user["username"] == username and user["password"] == hashed_password:
            found_user = user
            break

    if found_user:
        print("User found!")
        print("Role:", found_user["role"])
        print("Access Level:", found_user["access_level"])

        resource = "Confidential Security Report"

        if resource == "Public Security Report":
            required_level = 1
        elif resource == "Confidential Security Report":
            required_level = 3
        elif resource == "Admin Configuration":
            required_level = 5

        result = "PENDING"

        print("Resource:", resource)

        if found_user["access_level"] >= required_level:
            result = "GRANTED"
            print("Access granted!")

            log_entry = (
                f"{datetime.now()} | Attempt: {attempt} | "
                f"{username} | {resource} | {result}\n"
            )

            with open("Scripts/access_log.txt", "a") as log_file:
                log_file.write(log_entry)

            break

        else:
            print("Access denied - insufficient access level.")
            result = "DENIED"

            log_entry = (
                f"{datetime.now()} | Attempt: {attempt} | "
                f"{username} | {resource} | {result}\n"
            )

            with open("Scripts/access_log.txt", "a") as log_file:
                log_file.write(log_entry)

    else:
        print("Access denied - invalid username or password.")
        result = "DENIED"

        failed_attempts += 1
        print("Failed attempts:", failed_attempts)

        resource = "Confidential Security Report"

        log_entry = (
            f"{datetime.now()} | Attempt: {attempt} | "
            f"{username} | {resource} | {result}\n"
        )

        with open("Scripts/access_log.txt", "a") as log_file:
            log_file.write(log_entry)

    attempt += 1

    if failed_attempts >= 3:
        print("Account locked due to multiple failed attempts.")
        break

if attempt > 3:
    print("Maximum login attempts reached.")



