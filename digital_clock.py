import turtle
import time

# turtle window
window = turtle.Screen()
window.title("Digital Clock")
window.bgcolor("black")
window.setup(width=600, height=350)

# set up the turtle for drawing text
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
clock_turtle.color("white")
clock_turtle.penup()
clock_turtle.goto(0, 0)
clock_turtle.speed(0)

# set up turtle for drawing date
date_turtle = turtle.Turtle()
date_turtle.hideturtle()
date_turtle.color("white")
date_turtle.penup()
date_turtle.goto(0, -30)
date_turtle.speed(0)

# setup turtle for frame around the clock
frame_turtle = turtle.Turtle()
frame_turtle.hideturtle()
frame_turtle.color("cyan")
frame_turtle.penup()
frame_turtle.goto(-270, 150)
frame_turtle.pendown()
frame_turtle.pensize(5)

# function to draw a colorful frame
def draw_colorful_frame():
    colors = ["cyan", "magenta", "yellow", "orange"]  # Four colors for four sides

    frame_turtle.pendown()
    for i in range(4):
        frame_turtle.color(colors[i])  # Change color for each side
        frame_turtle.forward(540 if i % 2 == 0 else 300)
        frame_turtle.right(90)

draw_colorful_frame()

# function to display time
def display_time_date():
    # current time  and date using time module
    current_time = time.strftime("%H: %M: %S")
    current_date = time.strftime("%Y-%m-%d")

    # clear previous drawings
    clock_turtle.clear()
    date_turtle.clear()

    # show current time and date
    clock_turtle.write(current_time, align="center", font=("Courier", 48 ,"bold"))
    date_turtle.write(current_date, align="center", font=("Courier", 24, "bold"))

    # schedule the function run again after 1 second (1000ms)
    window.ontimer(display_time_date, 1000)

display_time_date()

window.mainloop()
