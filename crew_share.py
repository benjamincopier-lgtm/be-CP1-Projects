#benjamin copier crew shares
import random
print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. They are trying to figure out how to divide the spoils up among themselves.")
while True:
    try:
        ravagers_with_leaders= int(input("how many ravagers are in the crew: "))
    except:
     print("not a number")
    else:
        break
credits_earned= random.randint(500,5000)
ravagers_without_leaders= ravagers_with_leaders- (2)
print(ravagers_without_leaders)
ravagers_first_cut= ravagers_without_leaders * (3)
new_credits= credits_earned -ravagers_first_cut