
contacts = {
    "Rama": "98839348",
    "Laxman": "756393932",
    "Hari": "738292022",
    "Gauri": "23780016643"
}

name = input("Enter the name to search: ")
name = name.title()

if name in contacts:
    print(f"{name}'s phone number is: {contacts[name]}")
else:
    print("User not found.")