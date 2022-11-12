from math import *
import turtle
from random import *

turtle.penup()
turtle.radians()



def drawpoints(point_1,point_2): #Draws the 2 points for the coords
    turtle.color("blue")
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.dot(7)
    turtle.color("green")
    turtle.setx(point_2[0])
    turtle.sety(point_2[1])
    turtle.dot(7)
    turtle.sety(turtle.ycor()+3)

def drawangle(ship_angle, angle,point_1): #Draws the angles mathematically on the first point
    turtle.color("pink")
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(65)
    turtle.penup()
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.color("blue")
    turtle.setheading(ship_angle)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()

def redstonevalues(point_1,northredstone,southredstone,eastredstone,westredstone,shipangle): #Draws the points for each direction of the ship
    turtle.color("red")
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.setheading(radians(90)+shipangle)
    turtle.pendown()
    turtle.forward(northredstone*4)
    turtle.penup()
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.setheading(radians(270)+shipangle)
    turtle.pendown()
    turtle.forward(southredstone*4)
    turtle.penup()
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.setheading(radians(0)+shipangle)
    turtle.pendown()
    turtle.forward(eastredstone*4)
    turtle.penup()
    turtle.setx(point_1[0])
    turtle.sety(point_1[1])
    turtle.setheading(radians(180)+shipangle)
    turtle.pendown()
    turtle.forward(westredstone*4)
    turtle.penup()

#All code from now on is actually important. All code previously was purely visual, THIS IS IMPORTANT TO KEEP IN MIND!! 
# This is all you need to use the code and just want pure numbers or outputs
def get_angle(point_1, point_2): #Function that calculates the vector angle for the 2 coords
    angle = atan2(point_2[1] - point_1[1], point_2[0] - point_1[0]) #Subtracting 2 points returns a vector that can become a radian
    return angle


#Empty variables you can change if you comment out the block below
coord1 = []
coord2 = []
ship_angle = 0

#Randomizes the coordinates and angle of the ship. Comment out if you want manual control
coord1.insert(0,randint(-150,150))
coord1.insert(1,randint(-150,150))
coord2.insert(0,randint(-150,150))
coord2.insert(1,randint(-150,150))
ship_angle = radians(randint(0,360))

#Does the funny vector getting and does some interesting math to get the angle relative to the ship. I dunno how I did it, it just clicked
#Sorry if theres no real explanation, im just as cluless as you and it worked
ang = get_angle(coord1,coord2)
angle = radians(degrees(ang-ship_angle))


#Math for the output of each direction, very fancy. Fairly easy to read and making a function was too much pain for me. Can be simplified but im too scared to touch it
#Equations for each one below, put in desmos to see visually
#North = forward; y=round(15*max(0,sin(x)*sin(x)))
#South = backward; y=round(15*max(0,sin(x+pi)*sin(x+pi)))
#East = right; y=round(15*max(0,cos(x)*cos(x)))
#West = right; y=round(15*max(0,cos(x+pi)*cos(x+pi)))

north = round(15*max(0,sin(angle))*sin(angle))

south = round(15*max(0,sin(angle+pi))*sin(angle+pi))

east = round(15*max(0,cos(angle))*cos(angle))

west = round(15*max(0,cos(angle+ pi ))*cos(angle+ pi ))


#All the functions being used, extra fancy. These are all entirely visual and outputs for the numbers

print(north,south,east,west)
print(ang)
print(ship_angle)
print(angle)
drawpoints(coord1,coord2)
drawangle(ship_angle, ang,coord1)
redstonevalues(coord1,north,south,east,west,ship_angle)
turtle.hideturtle()
turtle.Screen().exitonclick()

