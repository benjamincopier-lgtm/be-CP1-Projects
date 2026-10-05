#Iteration: going through a collection of items one at a time, repeating the same action for each one
#For Loop: a loop that repeats code once for each item in a sequence (like a list) — used when you know what you're looping over
#Iterator variable: the variable that holds the current item during each pass through the loop — commonly named i, but can (and often should) be named something more descriptive, like color when looping over a list of colors
#Indentation after the colon tells Python which lines are inside the loop (and will repeat) versus which lines come after the loop and only run once, after it finishes — same rule as with conditionals
#Repetition: running the same block of code more than once — loops are how programs repeat actions without copying and pasting the same code over and over
#Met Condition: when a loop's condition evaluates to true, allowing it to continue or begin another pass
#Failed Condition: when a loop's condition evaluates to false, which is what causes the loop to stop
#Exit Condition: the condition that determines when a loop stops running — for a for loop, this is simply running out of items to iterate over
import time

cheeses=["gajhsdf","ash","sfhwsfds","askjhfakjaeddkfjehf"]
for cheese in cheeses:
    print(f"gsdjhg {cheese}")
gfdfdgfgf=["gfhcvcnbccncvcbvcnbvcmnbvnbvnccbvcbvcbvcnbvnbvcnbvbvcn","mnbmnmnb","mnbnbvbvbvnxbvxbvcnbvcnbnbvnbvmnbmnb","mnnbvbvvcvnhvbvbvmnb"]
for fhsadfj in gfdfdgfgf:
    print(f"sfkkjklk {fhsadfj}")
for i in range(2,21,2):
    print(i)
    time.sleep(0.8)
for i in range(20, -1, -1):
    print(i)
    time.sleep(1)
    if i == 13:
        print("sorry its lunch time")
        time.sleep(60)
print("kabloom")
for i in range():
    67
    

#numbmultipier=0

#for numb3 in range(1,):
#    numb4=numb3
#    while numbmultipier <= 12:
#        numbmultipier+=1
#        numbmultipier2 =numb4*numbmultipier
#        print(numbmultipier2)
#    print(numbmultipier2)