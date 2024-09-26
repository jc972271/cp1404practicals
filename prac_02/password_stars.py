"""
CP1404 - Practical 2
Code for inputting password
"""


def main():
    password_length = 8

    password = get_password(password_length)

    obfuscate_password(password)


def get_password(password_length):
    password = input('Enter your password: ')
    while len(password) < password_length:
        print(f"Password must be longer then {password_length} characters")
        password = input('Enter your password: ')
    return password


def obfuscate_password(password):
    print("*" * len(password))


main()
