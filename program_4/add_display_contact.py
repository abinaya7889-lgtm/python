contacts = []

name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

contact = {
    "name": name,
    "phone": phone,
    "email": email
}

contacts.append(contact)

print("\nContact Details")
for contact in contacts:
    print("Name:", contact["name"])
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])