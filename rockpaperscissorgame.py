import random

options=("rock", "paper","scissor")
running=True

while running:

    player=None
    computer=random.choice(options)


    while player not in options:
        player=input("Enter your choice (rock ,paper ,scissor): ")

    print(f"player: {player}")    
    print(f"computer: {computer}")    


    if player==computer:
        print(f"its a tie!")
    elif player=="paper" and computer=="rock":
        print(f"You win!")
    elif player== "scissor" and computer=="paper":
        print(f"You win!")
    elif player=="rock" and computer=="scissor":
        print(f"You win!")
    else:
        print(f"You loose!")

    if not input("play again? (y/n): ").lower()=="y":
        running=False

print(f"Thanks for playing!")
