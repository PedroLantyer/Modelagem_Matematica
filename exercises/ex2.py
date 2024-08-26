import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(x):
    return (pow(x,2) + (1/x) - 5)



def bisection(f, a, b, tolerance):
    if (f(a) * f(b) == 0):
            print("Fail")
            return None
    
    iterrationArr = []

    c = (a + b) / 2.0
    while(b - a) / 2.0 > tolerance:
        iterrationArr.append((a, b, c))
        if(f(c) == 0):
            return c
        elif(f(a) * f(c) < 0):
            b = c
        else:
            a = c

        c = (a + b) / 2.0

    return iterrationArr

def printArr(arr):
    for x in arr: print(x)


if __name__ == "__main__":
    intervalStart = 1e-4
    intervalEnd = 5
    tolerance = 1e-2

    iterationArr = bisection(f=f, a=intervalStart, b=intervalEnd, tolerance=tolerance)
    printArr(iterationArr)
