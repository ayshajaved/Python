# import turtle   #this is the already installed library

# def draw_heart():
#     window = turtle.Screen()
#     window.bgcolor("black")

#     pen = turtle.Turtle()
#     pen.color("red")
#     pen.begin_fill()

#     pen.left(50)
#     pen.forward(133)
#     pen.circle(50, 200)
#     pen.right(140)
#     pen.circle(50, 200)
#     pen.forward(133)

#     pen.end_fill()
#     pen.hideturtle()
#     window.mainloop()

# draw_heart()





import turtle
# canvas = turtle.Screen()
# canvas.bgcolor("red")
# pen = turtle.turtle()
# pen.color("black")
















# def draw_circle():
#     window = turtle.Screen()
#     window.bgcolor("white")  # You can change the background color

#     pen = turtle.Turtle()
#     pen.color("blue")  # You can change the pen color
#     pen.pensize(15)  # You can change the pen size
#     pen.begin_fill()
#     pen.circle(100)  # Draws a circle with a radius of 100 units
#     pen.end_fill()
#     pen.hideturtle()
#     window.mainloop()

# draw_circle()

# import turtle

# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor("white")  # You can change the background color

#     pen = turtle.Turtle()
#     pen.color("blue")  # You can change the pen color
#     pen.pensize(2)  # You can change the pen size

#     for _ in range(4):
#         pen.forward(100)  # Move forward by 100 units
#         pen.right(90)     # Turn right by 90 degrees

#     pen.hideturtle()
#     window.mainloop()

# draw_square()

import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(-100)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
