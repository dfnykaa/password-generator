import random
import string

def create_password(length=16):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def save_password(account, password):
    with open("passwords.txt", "a") as f:
        f.write(f"Account: {account} | Password: {password}\n")