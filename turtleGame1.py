from turtle import *

t = Turtle()
screen = t.getscreen()
t.penup()
t.goto(screen.window_width() / 2 - 200, screen.window_height() / 2-50)
t.hideturtle()
score = 0

def updatescore():
	t.clear()
	t.write("Score: " + str(score), False, "left", font=("Arial", 20, "normal"))

updatescore()

screen.mainloop()

