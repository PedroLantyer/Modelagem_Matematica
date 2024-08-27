import math
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.animation import FuncAnimation

def clearTerminal():
    if(os.name.upper() == "NT"):
        os.system("cls")

def f(height):
    #V = PI * h**2 * ((3r - h)/3)
    radius = 3
    volume = 30
    return (math.pi * pow(height,2) * (((3*radius) - height) / 3) - volume)

def bisection(f, a, b, tolerance):
        try:
            a, b, = a, b
            if (f(a) * f(b) == 0):
                raise Exception("Fail")
            
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
        
        except Exception as err:
            print(err)
            return None

def printArr(arr):
    for i in range(len(arr)):
        print(f"A: {arr[i][0]:.5f}, B: {arr[i][1]:.5f}, C:{arr[i][2]:.5f}")

def drawGraph(f, data: list, animationTimer:int = 2000):
    try:
        # Prepare the plot
        figure, ax = plt.subplots()
        x = np.linspace(1e-5, 3, 200)

        y = f(x)
        ax.plot(x, y, 'b-', label='f(x)')
        ax.axhline(0, color='black', lw=0.5)
        line, = ax.plot([], [], 'ro-', lw=2)
        text = ax.text(0.5, 0.5, '', transform=ax.transAxes, ha='center')

        # Set up the plot limits and labels
        ax.set_xlim(0, 5) #Set limits for the X axis
        ax.set_ylim(min(y), max(y))

        ax.set_xlabel('x') #Set label For X axis
        ax.set_ylabel('f(x)') #Set label for Y axis
        ax.legend()

        # Animation update
        def update(i):
            a, b, c = data[i]
            line.set_data([a, b], [f(a), f(b)])
            text.set_text(f'Iteration {i+1}: c = {c:.5f}')
            return line, text
        
        ani = FuncAnimation(figure, update, frames=len(data), interval=animationTimer, repeat=False)

        plt.show()
    
    except Exception as err:
        print(err)

if __name__ == "__main__":
    clearTerminal()
    a = 1e-5
    b = 3.0
    tol = 1e-5

    iterationArr = bisection(f=f, a=a, b=b, tolerance=tol)
    printArr(iterationArr)

    drawGraph(f=f, data=iterationArr, animationTimer=1000)
