"""
CP1404 - Practical 5
Get name from email
"""

email = input("Email: ")
email_to_name = {}

while email != "":
    name = " ".join(email.split("@")[0].split(".")).title()
    choice = input(f"Is your name {name} (Y/n)?").lower()
    if choice == "y" or choice == "":
        email_to_name[email] = name
    else:
        name = input("Name: ")
        email_to_name[email] = name

    email = input("Email: ")

for key in email_to_name:
    print(f"{email_to_name[key]} ({key})")
