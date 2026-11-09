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
time.sleep(5)
turtle_green.goto(-100,0)
turtle_purple=t.Turtle()
turtle_purple.shape("turtle")
turtle_purple.penup()
turtle_purple.color("purple")
turtle_purple.speed(6)
turtle_purple.goto(-100,40)
turtle_blue=t.Turtle()
turtle_blue.shape("turtle")
turtle_blue.penup()
turtle_blue.color("blue")
turtle_blue.speed(9)
turtle_blue.goto(-100,80)
turtle3=t.Turtle()
turtle_green.shape("turtle")
turtle3.penup()
turtle3.color("red")
turtle3.speed(48)
turtle3.goto(-100,120)
time.sleep(3)
while turtle_green != 400 or turtle1 != 400 or turtle_blue != 400 or turtle3 !=400:
    turtle_purple.forward(numbers)
    turtle_blue.forward(numbers2)
    turtle_green.forward(numbers3)
    turtle_red.forward(numbers4)




t.exitonclick
