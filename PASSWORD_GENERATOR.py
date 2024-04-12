import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password


password_length = int(input("Give length of password: "))
strong_password = generate_strong_password(password_length)
print(f"Generated strong password: {strong_password}")
