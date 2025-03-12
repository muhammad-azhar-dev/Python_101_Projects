import string
import random

length = int(input("Enter the password length: "))
characters = string.ascii_letters + string.digits+ string.punctuation
password = ''.join(random.choices(characters, k=length))
print(f"Generated password: {password}")