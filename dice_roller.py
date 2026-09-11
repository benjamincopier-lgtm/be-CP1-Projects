#benjamin copier dice roller

import random
while True:
    try:
        dicetype=int(input("choose between a 4 a 6 a 8 a 10 a 12 and a 20: "))
    except:
     print("your number of sides in numerical digits")
    else:
        break
dice_chosen=random.randint(1,dicetype)
sdice_chosen=str(dice_chosen)
print("you rolled a nat "+sdice_chosen)