import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter password length (8-25): "))
        if 8 <= length <= 25:
            break
        else:
            print("Password length must be between 8 and 25.")
    except ValueError:
        print("Please enter a valid number.")

password = generate_password(length)
print(f"Generated Password: {password}")