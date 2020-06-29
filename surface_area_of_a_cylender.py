''' Here we will find the surface area of a cylender '''

from math import pi
r = int(input("radius of the cylinder:- "))
h = int(input("height of the cylinder:- "))

surface = 2*pi*r*(h+r)
print(surface)
