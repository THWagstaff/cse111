
#x=5
#y=6
#print(y != x and x ==y)
#False

#name = 'Joey'
#print("J" in name)
#true (Looking for "J" in name variable)

import math

#declares radius
def computeCircumference(radius):
     return math.pi * radius * 2

x = int(input("please enter a number: "))

circumference = computeCircumference(x)

print(circumference)