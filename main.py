from turtle import *
import random
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"
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
def move_with_heading(t,turtles):
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
        turtles.append(duplicate())
    if t.ycor()> 290 or t.ycor() < -290:
        t.setheading(t.heading()*-1)
        t.forward(10)
        turtles.append(duplicate())
    return turtles
def duplicate():
    t=Turtle()
    t.color(generate_color())
    t.speed(0)
    t.penup()
    t.shape("circle")
    t.setheading(random.randint(0,360))
    return t
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
def create_player():
    global player
    player= Turtle()
    player.speed(0)
    player.pensize(3)
    player.color(generate_color())
    player.shape("turtle")
def up():
    global player
    player.setheading(90)
    player.forward(10)
def down():
    global player
    player.setheading(-90)
    player.forward(10)
def right():
    global player
    player.right(5)
def left():
    global player
    player.left(5)

playing_area()
player = None
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.listen()
screen.onkey(create_player, "space" )
# screen.onkeypress(up,"w")
# screen.onkeypress(down,"s")
screen.onkeypress(right,"d")
screen.onkeypress(left,"a")
t=Turtle()
t.color(generate_color())
t.speed(0)
t.penup()
t.shape("circle")
t.setheading(random.randint(0,360))
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)
turtles=[t]


screen.tracer(100)
alive= True
while alive:
    screen.update()
    if player!= None :
        move_with_heading(player,turtles)
    for obj in turtles:
        move_with_heading(obj,turtles)
        if player!= None and player.distance(obj)<20:
            obj.hideturtle()
            turtles.remove(obj)






screen.exitonclick()
