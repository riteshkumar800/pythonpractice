def show_balance(balance):
    print(f"your balance is ${balance: .2f}")


def deposit():
    amount=float(input("Enter an amount to be deposited: "))

    if amount<0:
        print(f"thats not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount=float(input("Enter the amount to be withdraw: "))

    if amount>balance:
        print(f"insufficient funds")
        return 0
    elif amount<0:
        print(f"amount must be greater than 0")
    else:
        return amount



def main():
    balance=0
    is_running=True


    while is_running:
        print(".  Bankiing Program.  ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")


        choice=input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+=deposit(balance)
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            is_running= False
        else:
            print("That is not a Valid choice") 


print("Thanku U have a Nice day!")

if __name__=='__main__':
    main()
    






