questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")

guesses=[]
score=0
question_num=0

for question in questions:
    print(question)
    print(f"-----------------------")
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A, B, C, D): ") 
    guesses.append(guess.upper())
    if guesses[question_num]==answers[question_num]:
        print(f"CORRECT")
        score+=1
    else:
        print(f"INCORRECT")
        print(f"{answers[question_num]} is the correct")

       

    question_num+=1   




print(f"-----------------------")     
print(f"RESULTS ")  
print(f"-----------------------") 

print(f"answers",end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print(f"guesses",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()    

score=int(score/len(questions)*100)
print(f"your score is: {score}%")    
