import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("black")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
angle=120
for i in range(3):
    for counter in range(1,4):
        alex.circle(20*counter)
    alex.right(angle)
    if(i==0):
        alex.color("blue")
    elif(i==1):
        alex.color("red")


#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern
