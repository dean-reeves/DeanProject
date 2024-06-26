# generate_random_username.py
import random
import string

def generate_username(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter the length of the username: "))
    username = generate_username(length)
    print(f"Generated username: {username}")
