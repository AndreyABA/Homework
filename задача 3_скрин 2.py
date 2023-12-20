import math
def findradius(v):
    radius = ((3 * v) / (4 * math.pi))**(1/3)
    return radius
v = 477457547
r = findradius(v)
print(f"Радиус сферы: {r}")