#Benjamin copier order up
# psuedocode the first 19 lines are for librarys, lines 21-25 are for price calculation, all lines from 29-112 are for collecting order. they all are structured the same, and the structure starts with setting ordering to true , we then enter a while loop controlled by the ordering variable, we now ask for an input and we see whether or not it is in the library, if its not they restart, if it is they are asked to give a number. if they give a number we use it to determine price, if not they retry
 
sides= {
    "cheese curds":  50,
    "onion rings": 100,
    "nuggets": 200,
    "fries": 50
}
main_course= {
    "burger": 300,
    "chicken sandwich": 500,
    "fish sandwich": 600,
    "big mac": 700
}
drink={
    "fountain drink":150,
    "water":20,
    "lemonade":100,
    "hot chocolate": 200
}
def price(item1,item2,item3,item4):
    total_p = 0
    total_p += item1 + item2 + item3 + item4
    return total_p
    
    

keys=list(sides.keys())
for key in keys:
    print(f"the sides and prices are {key} it is {sides[key]} cents")
ordering= True
while ordering== True:
    side_chosen=input("what side do you want in your meal: ")

    if side_chosen in sides:
        while True :
            try:
                side_numb=int(input("how many do you want: "))
                price1=side_numb*sides[side_chosen]
                total1=(f"you wanted {side_numb} {side_chosen} and spent {price1}")
            except:
                print("you need a number")
            else:
                break
        ordering=False
    else:
        print("not on the menu")
        ordering=True
keys=list(main_course.keys())

keys=list(sides.keys())
for key in keys:
    print(f"the sides and prices are {key} it is {sides[key]} cents")
ordering= True
while ordering== True:
    side_chosen=input("what side do you want in your meal: ")

    if side_chosen in sides:
        while True :
            try:
                side_numb=int(input("how many do you want: "))
                price4=side_numb*sides[side_chosen]
                total4=(f"you wanted {side_numb} {side_chosen} and spent {price4}")
            except:
                print("you need a number")
            else:
                break
        ordering=False
    else:
        print("not on the menu")
        ordering=True
keys=list(main_course.keys())
for key in keys:
    print(f"the main course and price is {key} it is {main_course[key]} cents")
ordering= True
while ordering== True:
    main_course_chosen=input("what main course do you want in your meal: ")
    if main_course_chosen in main_course:
        while True :
            try:
                main_numb=int(input("how many do you want: "))
                price2=main_numb*main_course[main_course_chosen]
                total2=(f"you wanted {main_numb} {main_course_chosen}(s) and spent {price2} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
    else:
        print("not on the menu")
        ordering=True
keys=list(drink.keys())
for key in keys:
    print(f"the main course and price is {key} it is {drink[key]} cents")
ordering= True
while ordering== True:
    drink_chosen=input("what drink do you want in your meal: ")
    if drink_chosen in drink:
        while True :
            try:
                drink_amount=int(input("how many do you want: "))
                price3=drink_amount*drink[drink_chosen]
                total3=(f"you wanted {drink_amount} {drink_chosen}(s) and spent {price3} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
    else:
        print("not on the menu")
        ordering=True
final = price(price1, price2, price3,price4)
print(f"{total1} for your first side")
print(f"{total4} for your second side,")
print(f"{total2}")
print(f"{total3}.")
print(f" in total you spent {final} cents")