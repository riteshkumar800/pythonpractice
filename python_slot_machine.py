import random

def spin_now():
    symbols=['✨','🎉','🧐','🍒','🥭']
    return [random.choice(symbols) for _ in range(3)]

def print_now(row):
    print(' | '.join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        symbol=row[0]

        if symbol=='🍒':
            return bet*3
        if symbol=='🥭':
            return bet*4
        if symbol=='🧐':
            return bet*5
        if symbol=='🎉':
            return bet*10
        if symbol=='✨':
            return bet*20

    return 0

def main():
    balance=100

    print("Welcome to Python Slots")
    print("Symbols: ✨ 🎉 🧐 🍒 🥭")

    while balance>0:
        print(f"\nCurrent balance: ${balance}")

        bet=input("Place your bet amount: ")

        if not bet.isdigit():
            print("Enter a valid amount")
            continue

        bet=int(bet)

        if bet>balance:
            print("Insufficient balance")
            continue

        if bet<=0:
            print("Bet must be greater than 0")
            continue

        balance-=bet

        row=spin_now()
        print("Spinning...")
        print_now(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance+=payout

        play_again=input("Do you want to spin again? (Y/N): ").upper()

        if play_again!='Y':
            break

    print(f"\nYour final balance is ${balance}")

if __name__=='__main__':
    main()
