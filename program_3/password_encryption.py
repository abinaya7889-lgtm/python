password = input("Enter your password: ")

encrypted = ""

for ch in password:
    encrypted += chr(ord(ch) + 3)

print("Original Password:", password)
print("Encrypted Password:", encrypted)