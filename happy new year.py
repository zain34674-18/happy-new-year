import turtle
import random
import math
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("midnight blue")
screen.title("Happy New Year Fireworks")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# -------- Opening Scene --------
def opening_scene():
    pen.color("gold")
    pen.penup()
    pen.goto(0, 40)
    pen.write("✨ Welcome ✨", align="center", font=("Arial", 32, "bold"))

    pen.goto(0, -10)
    pen.color("light cyan")
    pen.write("A New Year, New Hopes, New Smiles", align="center",
              font=("Arial", 18, "normal"))

    time.sleep(2)
    pen.clear()

# -------- Firework Burst --------
fire = turtle.Turtle()
fire.hideturtle()
fire.speed(0)
fire.width(2)

def draw_firework(x, y):
    colors = ["red", "yellow", "cyan", "magenta", "orange", "lime", "white"]
    fire.penup()
    fire.goto(x, y)
    fire.pendown()

    color = random.choice(colors)
    for i in range(24):
        fire.color(color)
        fire.forward(120)
        fire.backward(120)
        fire.right(15)

# -------- Firework Animation --------
def fireworks_show():
    for _ in range(8):
        x = random.randint(-300, 300)
        y = random.randint(0, 200)
        draw_firework(x, y)
        time.sleep(0.6)

# -------- Greeting --------
def show_message():
    pen.color("gold")
    pen.goto(0, -200)
    pen.write("🎉 HAPPY NEW YEAR! 🎉",
              align="center",
              font=("Arial", 28, "bold"))

# Run the animation
opening_scene()
fireworks_show()
show_message()

turtle.done()
 