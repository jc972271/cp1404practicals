"""
CP1404 - Practical 2
Code for inputting password
"""
password_length = 8
password = input('Enter your password: ')

while len(password) < password_length:
    print(f"Password must be longer then {password_length} characters")
    password = input('Enter your password: ')

print("*" * len(password))
