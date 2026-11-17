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
keys=list(sides.keys())
for key in keys:
    print(f"the sides and prices are {key} it is {sides[key]} cents")
ordering= True
while ordering== True:
    steven=input("what side do you want in your meal: ")
    if steven in sides:
        while True :
            try:
                steven2=int(input("how many do you want: "))
                steven7=steven2*sides[steven]
                print(f"you wanted {steven2} {steven} and spent {steven7} cents")
                steven4=(f"you wanted {steven2} {steven} and spent {steven7} cents")
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
    steven=input("what main coarse do you want in your meal: ")
    if steven in main_coarse:
        while True :
            try:
                steven2=int(input("how many do you want: "))
                steven6=steven2*main_coarse[steven]
                print(f"you wanted {steven2} {steven} and spent {steven6} cents")
                steven5=(f"you wanted {steven2} {steven} and spent {steven6} cents")
            except:
                print("you need a number")
            else:
                break
        ordering=False
steven8=steven6+steven7
print(f"{steven4} for your side and {steven5} for your main coarse. in total you spent {steven8}")
