"""
CP1404 - Practical 2
Code for inputting password
"""


def main():
    """Get a password and return an obfuscate result."""
    password_length = 8

    password = get_password(password_length)

    obfuscate_password(password)


def get_password(password_length):
    """Get user password."""
    password = input('Enter your password: ')
    while len(password) < password_length:
        print(f"Password must be longer then {password_length} characters")
        password = input('Enter your password: ')
    return password


def obfuscate_password(password):
    """Return a string of stars equal in length to an inputted string."""
    print("*" * len(password))


main()
