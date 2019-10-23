from turtle import *

t1=Turtle()

screen = t1.getscreen()

t1.forward(10)

def writeName():
	name = screen.textinput("name","What is your name?")
	t1.write(name, move=True,align="left", font=("Arial",30,"normal"))
	
	screen.listen()
screen.onkey(writeName, "w")

screen.listen()
screen.mainloop()

