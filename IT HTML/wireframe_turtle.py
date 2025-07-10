import turtle

screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.title("Wireframe Design")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

def draw_box(x, y, width, height, label, color):
    pen.penup()
    pen.goto(x, y)
    pen.color("black", color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(x + width / 2, y - height / 2)
    pen.write(label, align="center", font=("Arial", 12, "bold"))

draw_box(-250, 350, 500, 80, "Header (Logo + Slider)", "skyblue")
draw_box(-250, 260, 500, 40, "Navigation Bar", "lightcoral")
draw_box(-250, 210, 320, 400, "Main Content", "lightgreen")
draw_box(70, 210, 180, 400, "Sidebar", "khaki")
draw_box(-250, -230, 500, 80, "Footer", "lightgray")

pen.hideturtle()
turtle.done()