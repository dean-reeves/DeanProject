# func_py_generate_password.py
import random
import string

def generate_password(length=12):
    """
    Generate a random password of specified length.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password(16)
    print(f"Generated Password: {password}")
