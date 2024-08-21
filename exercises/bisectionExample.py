import os
import numpy

def clearScreen():
    try:
        if(os.name.upper() == "NT"):
            os.system("cls")
    except Exception as err:
        print(err)

def f(x):
    return (pow(x,3) -x -2)

def bisection(f, a, b, toi):
    if (f(a) + f(b)) == 0:
        print("Fail")
        return None
    
    c = (a+b)/2.0
    while(b - a)/ 2.0 > toi:
        if(f(c) == 0):
            return c
        elif(f(a) * f(c) < 0):
            b = c
        else:
            a = c
        c = (a+b)/2.0
    
    return c

if __name__ == "__main__":
    clearScreen()
    a = 3
    b = -5
    toi = 0.1
    print(bisection(f, a, b, toi))