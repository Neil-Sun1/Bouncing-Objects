from turtle import *
import random


# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


# Creates the rectangular game boundary
def playing_area():
    # Draw a filled rectangle that covers most of the screen,
    # leaving approximately a 20-pixel margin on all sides.
    t= Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(generate_color())
    t.goto(-290,-290)
    t.begin_fill()
    t.goto(285,-290)
    t.goto(285,290)
    t.goto(-290, 290)
    t.goto(-290,-290)
    t.end_fill()
    pass

# Function 1: Movement using turtle heading (forward + setheading)
def move_with_heading(t):
    # Move the turtle continuously using forward movement and its current heading.
    # The turtle should update its position each frame using forward().
    # When the turtle hits a boundary:
    #   - Use heading() to check its current direction.
    #   - Calculate the reflection angle based on the wall it hits.
    #   - Use setheading() to update the direction so it "bounces" off the wall.
    # The result should be smooth motion where direction is controlled by angles.
    t.forward(5)

    if t.xcor()> 285 or t.xcor() < -290:
        t.setheading(180-t.heading())
        t.forward(10)
    if t.ycor()> 290 or t.ycor() < -290:
        t.setheading(t.heading()*-1)



# Function 2: Movement using delta x / delta y (coordinate-based movement)
def move_with_deltas(t, deltax, deltay):
    # Move the turtle by directly updating its x and y position using dx and dy values.
    # Each update step:
    #   - Add deltax to x-coordinate and deltay to y-coordinate.
    # When the turtle hits a boundary:
    #   - Reverse deltax if it hits a left/right wall.
    #   - Reverse deltay if it hits a top/bottom wall.
    # This creates a bounce effect using vector-style movement instead of angles.
    # The turtle’s position should be updated using setx() and sety().
    newX= t.xcor() + deltax
    newY= t.ycor() + deltay


    if newX > 285 or newX <-290:
        newX = t.xcor()
        deltax *=-1
    if newY > 290 or newY <-290:
        newY = t.ycor()
        deltay *=-1
    
    t.goto(newX,newY)
    return deltax, deltay
playing_area()

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
t=Turtle()
t.color(generate_color())
t.speed(0)
t.shape("circle")
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)



alive= True
while alive:
    deltax,deltay = move_with_deltas(t,deltax,deltay)




screen.exitonclick()
