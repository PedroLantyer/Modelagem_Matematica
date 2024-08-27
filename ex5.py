import os
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 9.81

def f(mass):
    c = 15 #kg/s
    t = 9 #seconds
    return G * (mass / c) * (1 - pow(c, (-(c/mass) * t))) - 36

def df(mass):
    c = 15
    t = 9
    #part2 = 15 ** (-(15/mass) * 9)
    #part2 = ((-(15/mass) * 9) * 15) ** ((-(15/mass) * 9) - 1)
    #part2 = ((-(15/9) * mass) * 15) ** ((-(15/9) * mass) -1)
    #part2 = (-(15*15/9) * mass) ** ((-(15/9) * mass) -1)
    
    #9.81 * (mass / 15) * (1 - part2) - 0
    #(9.81 / 15) * mass * ((1 - part2) * (x**0))
    #(9.81 / 15) * mass * (1 - part2)
    return ((G / c) * mass * (1 - (-(c*c/t) * mass) ** ((-(c/t) * mass) -1)))

def newton_raphson(f, df, x0: float, tolerance:float = 0.1, max_iter:int = 100):
    iterations = 0

    while(iterations < max_iter):
        x1 = x0 - f(x0) / df(x0)    
        if abs(f(x1)) < tolerance:
            return [x1, (iterations+1)]
        x0 = x1
        iterations += 1
    return [x0, iterations]

if __name__ == "__main__":
    x0 = 1 #Place holder
    res = newton_raphson(f=f, df=df, x0=x0)
    value, iter = res[0], res[1]
    print(f"Value: {value}")
    print(iter)
