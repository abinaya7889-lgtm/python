balance = 5000

amount = int(input("Enter transfer amount: "))

if amount <= balance:
    balance -= amount
    print("Money Transfer Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")