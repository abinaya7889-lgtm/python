pin = 1234

old_pin = int(input("Enter old PIN: "))

if old_pin == pin:
    new_pin = int(input("Enter new PIN: "))
    pin = new_pin
    print("PIN Changed Successfully")
else:
    print("Wrong PIN")