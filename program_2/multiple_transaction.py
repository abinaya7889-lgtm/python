balance = 5000

while True:
    print("\n1.Balance 2.Deposit 3.Withdraw 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        balance += int(input("Deposit: "))
        print("Balance:", balance)

    elif choice == 3:
        amount = int(input("Withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You!")
        break