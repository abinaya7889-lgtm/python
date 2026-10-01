contacts = []

n = int(input("Enter number of contacts: "))

for i in range(n):
    print("\nContact", i + 1)

    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

print("\n--- Contact List ---")

for contact in contacts:
    print(contact)