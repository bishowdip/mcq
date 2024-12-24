
balance = 5000
print("welco,e to the ATM!")
print("1. Balance Inquiry")
print("2. Withdraw cash")
print("3. Deposit cash")
print("4. Exit")
choice = int(input("please enter your choice(1-4): "))
if choice == 1:
    print(f"your curent balance is: {balance}")
elif choice == 2:
    amount = int(input("Enter a amount to withdraw: "))
    if amount > balance:
        print("insufficient fund,") 
    else:
        balance -= amount
        print(f"withdraw successful! your new balance is: {balance}")
elif choice == 3:
    amount = int(input("enter a amount to deposit: "))
    if amount <= 0:
        print("invalid amount. please enter a positiive value.")
    else:
        balance += amount
        print(f"Deposit successful ! your new balance is: {balance}")
elif choice == 4:
    print("Thank you for using the ATM. Goodbye!")
else:
    print("invalid choice. Please try again.")
    