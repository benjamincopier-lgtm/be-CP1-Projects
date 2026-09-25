#benjamin copier crew shares
import random
print("Yondu Udonta and his crew arrive at the Iron Lotus after several weeks of plundering various places around the galaxy. The crew has been in space for nearly six months and they are ready for a night of celebration. They are trying to figure out how to divide the spoils up among themselves.")
while True:
    try:
        ravagers_with_leaders= int(input("how many ravagers are in the crew including peter and yondu: "))
    except:
     print("not a number")
    else:
        break
credits_earned= random.randint(500,5000)
ravagers_without_leaders= ravagers_with_leaders- (2)
ravagers_first_cut= ravagers_without_leaders * (3)
new_credits= credits_earned -ravagers_first_cut
one_percent_of_new_credits= new_credits /100 
yondus_cut= 13* one_percent_of_new_credits
rounded_yondus_cut= round(yondus_cut,2)
new_credits2= new_credits-rounded_yondus_cut
one_percent_of_new_credits2=new_credits2/100
peters_cut= one_percent_of_new_credits2 *11
rounded_peters_cut= round(peters_cut,2)
new_credits3= new_credits2-rounded_peters_cut
ravagers_with_leaders_cut= new_credits3/ ravagers_with_leaders
rounded_ravagers_with_leaders_cut=round(ravagers_with_leaders_cut, 2)
yondus_new_cut= rounded_yondus_cut + rounded_ravagers_with_leaders_cut
peters_new_cut=rounded_peters_cut + rounded_ravagers_with_leaders_cut
rounded_peters_new_cut= round(peters_new_cut,2)
yondus_rounded_new_cut=round(yondus_new_cut,2)
print("we found", credits_earned)
print( f"all of the ravagers have at least gotten ",rounded_ravagers_with_leaders_cut)
print(f"peter in total got ", rounded_peters_new_cut)
print(F"yondu got in total " , yondus_rounded_new_cut)