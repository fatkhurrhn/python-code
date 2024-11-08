import turtle
import random
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks Simulation")
screen.setup(width=800, height=600)

# Turtle setup
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)
firework.width(2)

# Draw a single firework explosion
def draw_firework(x, y, colors):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    
    for _ in range(36):  # 36 lines for a full explosion
        firework.color(random.choice(colors))
        firework.forward(100)
        firework.backward(100)
        firework.right(10)

# Generate random colors for each firework
def generate_colors():
    colors = []
    for i in range(10):
        colors.append(colorsys.hsv_to_rgb(random.random(), 1, 1))  # Random bright color
    return colors

# Main animation loop
def firework_show():
    screen.tracer(0)  # Disable animation for faster updates
    for _ in range(10):  # Display 10 fireworks
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        colors = generate_colors()
        draw_firework(x, y, colors)
        screen.update()  # Manually update screen
        screen.clear()  # Clear after each firework
    
    screen.bye()  # Close window after show is done

# Run the firework show
firework_show()
