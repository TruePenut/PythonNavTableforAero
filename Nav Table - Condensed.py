#This is the version of the code with pure logic, not outputs or visualisation, just math and code

from math import *
from random import *

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

#Grand total of actual lines of code needed to run the program isssssssssssssssssssssssssssss
#20!
#Idk how its this small but its fine
