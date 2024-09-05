'''
A python module to exhibit the use of the __main__ name.
'''

import random
import math

def Leibniz(n): 
    pi = 0
    for j in range(1, n):
        pi += ((-1)**(j+1))/((2*j) - 1)
    return (4*pi)
    
def Sharp(n): 
    pi = 0
    for j in range(0, n):
        pi += (2 * (-1)**(j) * 3**(0.5-j))/(2*j + 1) 
    return pi

def Monte_Carlo(n):
    in_circle = 0
    out_circle = 0
    j = 0
    while j <= n:
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) < 1.0 : # Finding if the randomly generated point is within the circle or not 
            in_circle += 1 
        else : 
            out_circle += 1
        # Noting that the ratio of the number of in circle points to the number of out circle points should come to approximate the area of a quarter 
        # circle of radius 1 over a square of side length 1, we can obtain an expression for Pi. 
        j = j + 1
    pi = (in_circle / (in_circle + out_circle) * 4)
    return pi

def main(n):
    print(Leibniz(n))
    print(Sharp(n))
    print(Monte_Carlo(n))
    
# main is called once when the script is executed.    



