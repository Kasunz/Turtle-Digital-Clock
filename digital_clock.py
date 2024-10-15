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
def display_time():
    # current time using time module
    current_time = time.strftime("%H: %M: %S")
    clock_turtle.clear()

    # show current time
    clock_turtle.write(current_time, align="center", font=("Courier", 48 ,"bold"))

    window.ontimer(display_time, 1000)

display_time()

window.mainloop()
