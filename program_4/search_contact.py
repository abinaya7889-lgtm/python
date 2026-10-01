contacts = [
    {"name": "Arun", "phone": "9876543210", "email": "arun@gmail.com"},
    {"name": "Priya", "phone": "9876501234", "email": "priya@gmail.com"},
    {"name": "Rahul", "phone": "9876512345", "email": "rahul@gmail.com"}
]

search_name = input("Enter name to search: ")

found = False

for contact in contacts:
    if contact["name"].lower() == search_name.lower():
        print("\nContact Found")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        found = True

if not found:
    print("Contact not found.")