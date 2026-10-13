#benjamin copier escape room

import random
chance_of_success= random.randint(1,100)
print(chance_of_success)
if chance_of_success == 99:
    success=True
else:
    success = False
if success == True:
    truth="water comes pooling up from the bottom and all of the fires are extinguished"
else:
    truth="it lands one slot away from success"
print(f"you wake in a room in which fires are visible through glass walls. they appear to be inching closer, with you being able to feel the fires. the floors are covered in gassoline and there is a small gap that the fire will be able to   reach you through. A door with a keypad with LETTERS is visible, with a sign on the door saying 'STATE your case', also in the room with you in it, there is a SLOT MACHINE with there being one pull available, and a sign says 'pull   for water'. you pull on the machines handle and "+ truth)
chance_of_success = str(chance_of_success)
if success == True:
    print("you win")
else:
    print("continue")

if success == False:
    inputed_choice= input("what do you input into the keypad: ")
    inputed_choice_2 = inputed_choice.strip().title()
    if inputed_choice_2 == "Nevada":
        print("you win")
    elif inputed_choice_2 == "Pee":
        print("you win by putting out the fires, how you did it i'm not sure.")
    elif inputed_choice_2 == chance_of_success:
        print("cheater, you still won, but you know what you did")
    else:
        print("think of the LASt place you went to.")
        inputed_choice= input("what do you input into the keypad: ")
        inputed_choice_2 = inputed_choice.strip().title()
        if inputed_choice_2 == "Nevada":
            print("you win")
        elif inputed_choice_2 == "Pee":
            print("you win by putting out the fires, how you did it i'm not sure.")
        elif inputed_choice_2 == chance_of_success:
            print("cheater, you still won, but you know what you did")
        else:
            print("i personally would NEVer skip an AD")
            inputed_choice= input("what do you input into the keypad: ")
            inputed_choice_2 = inputed_choice.strip().title()
            if inputed_choice_2 == "Nevada":
                print("you win")
            elif inputed_choice_2 == "Pee":
                print("you win by putting out the fires, how you did it i'm not sure.")
            elif inputed_choice_2 == chance_of_success:
                print("cheater, you still won, but you know what you did")
            else:
                print("Hell is between the churches and the golden shore of america")
                inputed_choice= input("what do you input into the keypad: ")
                inputed_choice_2 = inputed_choice.strip().title()
                if inputed_choice_2 == "Nevada":
                    print("you win")
                elif inputed_choice_2 == "Pee":
                    print("you win by putting out the fires, how you did it i'm not sure.")
                elif inputed_choice_2 == chance_of_success:
                    print("cheater, you still won, but you know what you did")
                else:
                    print("you are consumed by the fire, you should have thought harder")