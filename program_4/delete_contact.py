contacts = [
    {"name": "Arun", "phone": "9876543210"},
    {"name": "Priya", "phone": "9876501234"},
    {"name": "Rahul", "phone": "9876512345"}
]

name = input("Enter name to delete: ")

found = False

for contact in contacts:
    if contact["name"].lower() == name.lower():
        contacts.remove(contact)
        found = True
        print("Contact deleted successfully.")
        break

if not found:
    print("Contact not found.")

print("\nRemaining Contacts:")

for contact in contacts:
    print(contact)