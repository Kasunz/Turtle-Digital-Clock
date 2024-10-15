import turtle
import time

# turtle window
window = turtle.Screen()
window.title("Digital Clock")
window.bgcolor("black")
window.setup(width=600, height=300)

# set up the turtle for drawing text
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
clock_turtle.color("white")
clock_turtle.penup()
clock_turtle.goto(0, 0)
clock_turtle.speed(0)

# function to display time
def display_time():
    # current time using time module
    current_time = time.strftime("%H: %M: %S")
    clock_turtle.clear()

    # show current time
    clock_turtle.write(current_time, align="center", font=("Courier", 48 ,"bold"))

    window.ontimer(display_time, 1000)

display_time()

window.mainloop()
