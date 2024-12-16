import os
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sympy import *

G = 9.81
C = 15
T = 9
V = 36

def clearTerminal():
    if os.name.upper() == "NT":
        os.system("cls")

def f(mass):
    return G * (mass / C) * (1 - pow(C, (-(C/mass) * T))) - V

def df(mass):
    return -G * T * exp(-C*T/mass)/mass + G * (1 - exp(-C*T/mass))/C

def newton_raphson(f, df, x0: float, tolerance:float = 1e-1, max_iter:int = 100):
    iterations = 0

    while(iterations < max_iter):
        x1 = x0 - f(x0) / df(x0)    
        if abs(f(x1)) < tolerance:
            return [x1, (iterations+1)]
        x0 = x1
        iterations += 1
    return [x0, iterations]

def falPos(f, a:float, b:float, tolerance:float = 1e-1):
    if f(a) * f(b) >= 0:
        print("Falsa posição falhou")
        return None
    
    iterations = 0
    c = b - (f(b) * (b-a) / (f(b) - f(a)))
    while abs(f(c)) > tolerance:
        if f(c) == 0:
            return C
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = C
        iterations += 1
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
    
    return [c, iterations]

def getRelativeError(x, y):
    try:
        absoluteError = abs(x - y)
        relativeError = (absoluteError/x)*100
        return relativeError
    except Exception as err:
        print(err)
        return None

if __name__ == "__main__":
    clearTerminal()
    x0 = 1e-1
   
    newRaphResults = newton_raphson(f=f, df=df, x0=x0)
    newRaphValue, newRaphIter = newRaphResults[0], newRaphResults[1]
    print("Newton Raphson:")
    print(f"Value: {newRaphValue:.4f}")
    print(f"Iterations: {newRaphIter}",end="\n\n")

    falPosRes = falPos(f=f, a=x0, b=100)
    falPosValue, falPosIter = falPosRes[0], falPosRes[1]
    print("Falsa Posição:")
    print(f"Value: {falPosValue:.4f}")
    print(f"Iterations: {falPosIter}",end="\n\n")

    values = [newRaphValue, falPosValue]
    values.sort(reverse=True)
    
    relativeError = getRelativeError(x=values[0],y=values[1])
    print(f"Relative Error: {relativeError:.4f} %",end="\n\n")