#Build mini ATM logic : if pin is correct allow the user to withdraw or check balance.

atm_pin = 6592
balance = 35062.0

pin = int(input("Enter your 4 digit ATM pin number: "))

if pin == atm_pin:
    data = input("Enter 1 for Withdraw Cash\nEnter 2 for Checking Balance\n")

    if data == '1':
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            print("Processing..........")
            print("Transaction Successful")
        else:
            print("Insufficient Balance")

    elif data == '2':
        print(f"Your Account Balance is {balance}")

    else:
        print("Invalid Selection")

else:
    print("Entered Incorrect Pin")