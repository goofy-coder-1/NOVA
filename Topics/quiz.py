#python quiz game

questions = ("Which is the tallest mountain in the world?: ",
             "Where was Buddha Born?: ",
             "How many bones are there in human body?: ",
             "Who is the strongest?: ",
             "Which is the fastest animal in the world?: "
            )

options = (("A. MOUNT EVEREST", "B. K2", "C. KANCHANJUNGA", "D. ANNAPURNA"),
           ("A. AT HIS HOUSE", "B. LUMBINI", "C. HIMALAYAM JAVA", "D. JHAPA"),
           ("A. 208", "B. 555", "C. 206", "D. 67"),
           ("A. GOKU", "B. SAITAMA", "C. USSOP", "D. BEERUS"),
           ("A. CHEETAH", "B. TIGER", "C. ELEPHANT", "D. YOU WHEN YO MAMA CHASING YOU")
           )

answers = ("A", "B", "C", "C", "D")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("!CORRECT")
    else: 
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct option")
    question_num += 1


print("------------------")
print("-----RESULT-------")
print("------------------")

print("answers: ", end = " ")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end= " ")
for guess in guesses: 
    print(guess, end= " ")
print()

score = int(score/len(questions)*100)
print(f"Your score is: {score}%")