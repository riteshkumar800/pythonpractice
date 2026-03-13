import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num, highest_num)
guessess=0
is_running=True


print("Number gussing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess=input("enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        guessess+=1
        if guess<lowest_num or guess>highest_num:
           print(f"That number is out of range")
           print(f"Select a number between {lowest_num} and {highest_num}")

        elif guess<answer:
           print(f"Too Low! Try again")
        elif guess>answer:
           print(f"Too high!try again")
        else:
           print(f"CORRECT! the answer was {answer}")
           print(f"Number of guessess: {guessess}")
           is_running=False         

    else:
        print(f"Invalid Number")
        print(f"please select a number between {lowest_num} and {highest_num}")


