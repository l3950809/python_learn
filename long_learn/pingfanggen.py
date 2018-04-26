import math

def pingfanggen (a, b, c):
    x1 = (0-b + math.sqrt(b*b-4*a*c)) / (2*a)
    x2 = (0-b - math.sqrt(b*b-4*a*c)) / (2*a)
    return(x1,x2)
print (pingfanggen(2,3,1))


