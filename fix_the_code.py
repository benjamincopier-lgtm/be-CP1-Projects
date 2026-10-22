#ben copier 

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = 20#random.randint(1, 20)
    guesses = 0
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
        while True:
            try:
                guess >= 1
                guess <= 20
            except:
             print(f"the number is less than or equal to 20 and greater than or equal to 1 ")
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
print("\n--- Game Over ---")
print(f"Your guesses per round: " , scores)

total = 0
for score in scores:
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(1, rounds - 1):
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
name=input(f"what is your first name: ").strip().title()
print("hello " + name.strip().title())
while True:
    try:
        guess =int(input(f"Guess a number between 1 and 20: "))
    except:
     print(f"the number in numerical digits")
    else:
        break