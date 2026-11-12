#lhhfhdfajhslkjdafsakjhkjgdsalkjgfdlkjfdshfdlksajlkjhfdaskjlkjhfdjsalkhfalskdjfhalkjsdf


import turtle as t
import random as r
import time
numbers = r.randint(1,50)
numbers2=r.randint(1,50)
numbers3 = r.randint(1,50)
numbers4=r.randint(1,24)
numbers5 = r.randint(1,50)
def turtle_type(starl, color):
    starl.shape("turtle")
    starl.color(color)

def turtle_hercules(stanley, speed, stuart):
    stanley.penup()
    stanley.speed(speed)
    stanley.goto(-500,stuart)
turtle_purple=t.Turtle()
turtle_type(turtle_purple, "purple")
turtle_hercules(turtle_purple,6,40)
turtle_green=t.Turtle()

turtle_type(turtle_green, "green")
turtle_hercules(turtle_green,7,0)
turtle_blue=t.Turtle()
turtle_type(turtle_blue, "blue")
turtle_hercules(turtle_blue,9,80)
turtle_red=t.Turtle()
turtle_type(turtle_red, "red")
turtle_hercules(turtle_red,0,120)
turtle_orange=t.Turtle()
turtle_type(turtle_orange, "orange")
turtle_hercules(turtle_orange,4,160)
turtle_finish_line=t.Turtle()

turtle_finish_line.hideturtle()
turtle_finish_line.speed(0)
turtle_finish_line.penup()
turtle_finish_line.goto(400,0)
turtle_finish_line.pendown()
turtle_finish_line.left(90)
turtle_finish_line.forward(200)
turtle_finish_line.right(180)
turtle_finish_line.forward(400)
true_turtle_winner=False
def turtle_winner(turtle,carl):
      if turtle.xcor()>=400:
           print(carl,"won")
           return True
      else:
          return False
        
while true_turtle_winner==False:
    turtle_purple.forward(numbers)
    turtle_blue.forward(numbers2)
    turtle_green.forward(numbers3)
    turtle_red.forward(numbers4)
    turtle_orange.forward(numbers5)
    if turtle_winner(turtle_blue, "blue turtle"):
        break
    if turtle_winner(turtle_green,  "green turtle" ):
        break
    if turtle_winner(turtle_red, "red turtle"):
        break
    if turtle_winner(turtle_orange, "orange turtle"):
        break
    if turtle_winner(turtle_purple, "purple turtle"):
        break
t.exitonclick()