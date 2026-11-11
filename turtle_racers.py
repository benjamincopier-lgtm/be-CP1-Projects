#lhhfhdfajhslkjdafsakjhkjgdsalkjgfdlkjfdshfdlksajlkjhfdaskjlkjhfdjsalkhfalskdjfhalkjsdf


import turtle as t
import random as r
import time
numbers = r.randint(1,50)
numbers2=r.randint(1,50)
numbers3 = r.randint(1,50)
numbers4=r.randint(1,24)
turtle_green=t.Turtle()
turtle_green.shape("turtle")
turtle_green.color("green")
turtle_green.penup()
turtle_green.speed(7)

turtle_green.goto(-500,0)
turtle_purple=t.Turtle()
turtle_purple.shape("turtle")
turtle_purple.penup()
turtle_purple.color("purple")
turtle_purple.speed(6)
turtle_purple.goto(-500,40)
turtle_blue=t.Turtle()
turtle_blue.shape("turtle")
turtle_blue.penup()
turtle_blue.color("blue")
turtle_blue.speed(9)
turtle_blue.goto(-500,80)
turtle_red=t.Turtle()
turtle_red.shape("turtle")
turtle_red.penup()
turtle_red.color("red")
turtle_red.speed(48)
turtle_red.goto(-500,120)
turtle_orange=t.Turtle()
turtle_orange.shape("turtle")
turtle_orange.penup()
turtle_orange.color("orange")
turtle_orange.speed(48)
turtle_orange.goto(-500,160)
turtle_finish_line=t.Turtle()
turtle_finish_line.penup()
turtle_finish_line.hideturtle()
turtle_finish_line.speed(0)
turtle_finish_line.goto(400,0)
true_turtle_winner=False







def turtle_winner(turtle):
      if turtle.xcor()>=400:
           print(turtle,"won")
           return True
      else:
          return False
        
while true_turtle_winner==False:
    turtle_purple.forward(numbers)
    turtle_blue.forward(numbers2)
    turtle_green.forward(numbers3)
    turtle_red.forward(numbers4)
    turtle_orange.forward(numbers)
    if turtle_winner(turtle_blue):
        break
    if turtle_winner(turtle_green):
        break
    if turtle_winner(turtle_red):
        break
    if turtle_winner(turtle_orange):
        break
    if turtle_winner(turtle_purple):
        break