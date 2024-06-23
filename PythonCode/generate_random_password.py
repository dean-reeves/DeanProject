# generate_random_password.py
import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length must be at least 6")
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
