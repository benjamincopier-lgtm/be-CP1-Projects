#ben copier 

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")
guesses=0
for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)

    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:
                guess =int(input(f"Guess a number between 1 and 20: "))
            except:
             print(f"the number in numerical digits")
            else:
                break
        guesses = guesses + 1
        if guess == secret_number:
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    scores.append(guesses)
    guesses = 0

print("\n--- Game Over ---")
print(f"Your guesses per round: " , scores)
scores2=scores[1]+scores[2]+scores[0]


average = scores2 / 3
print("Your average guesses per round was " + str(round(average,2)))
rounds+=1
best_round = scores[0]
for i in range(1, rounds-1):
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
name=input(f"what is your first name: ").strip().title()
print("hello " + name.strip().title())