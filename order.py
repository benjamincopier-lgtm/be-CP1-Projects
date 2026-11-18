#Benjamin copier order up

sides= {
    "cheese curds":  50,
    "onion rings": 100,
    "nuggets": 200,
    "fries": 50
}
main_coarse= {
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
def price(menu, item, amount):
    
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
                total1=(f"you wanted {side_numb} {side_chosen} and spent {price1} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
keys=list(main_coarse.keys())
for key in keys:
    print(f"the main coarse and price is {key} it is {main_coarse[key]} cents")
ordering= True
while ordering== True:
    main_coarse_chosen=input("what main coarse do you want in your meal: ")
    if main_coarse_chosen in main_coarse:
        while True :
            try:
                main_numb=int(input("how many do you want: "))
                price2=main_numb*main_coarse[main_coarse_chosen]
                total2=(f"you wanted {main_numb}(s) {main_coarse_chosen} and spent {price2} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
keys=list(drink.keys())
for key in keys:
    print(f"the main coarse and price is {key} it is {drink[key]} cents")
ordering= True
while ordering== True:
    drink_chosen=input("what drink do you want in your meal: ")
    if drink_chosen in drink:
        while True :
            try:
                drink_amount=int(input("how many do you want: "))
                price3=drink_amount*drink[drink_chosen]
                total3=(f"you wanted {drink_amount}(s) {drink_chosen} and spent {price3} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
total_price=price2+price1+price3
print(f"{total1} for your side, {total2} for your main coarse and {total3}. in total you spent {total_price}")
