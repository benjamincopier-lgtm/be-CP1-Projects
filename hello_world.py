# Benjamin copier, hello world

#cx=choices (x=any number)
print("you wake up in a room tha you do not recognise, when you look around you see that there is a door to the left of you and a random person to the right of you")
name= input("they ask you 'hello whats your name': ")
print( "hello " + name + " my name is shelly i wll be helping you on this journey")
choices=input("do you wish to leave this room (hint you can use the word left to go left and vice verse with right): " )
if (choices == "left"):print("you walk out and you see that you are in a new city")
print("there are three paths one in front of you, one to the left of you, and one to the right of you")
choices=input("if you wish to go to the left type left, if you want to go to the right type right and if you want to go forward type front: " )
if (choices == "left"):print("you go to the left")
if (choices == "right"):print("you go to the right")
if (choices == "forward"):print