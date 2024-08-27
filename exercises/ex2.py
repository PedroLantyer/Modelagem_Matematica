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
    try:
        print("Iterations: ")
        for i in range(len(arr)):
            print(f"A: {arr[i][0]:.4f}, B: {arr[i][1]:.4f}, C: {arr[i][2]:.4f}")
        print("\n")
    except Exception as err:
        print(err)

    

if __name__ == "__main__":
    intervalStart = 1e-4
    intervalEnd = 5
    tolerance = 1e-4

    iterationArr = bisection(f=f, a=intervalStart, b=intervalEnd, tolerance=tolerance)
    printArr(iterationArr)


        # Prepare the plot
    fig, ax = plt.subplots()
    x = np.linspace(1e-4, 6, 200)

    print(x)
    y = f(x)
    ax.plot(x, y, 'b-', label='f(x)')
    ax.axhline(0, color='black', lw=0.5)
    line, = ax.plot([], [], 'ro-', lw=2)
    text = ax.text(0.5, 0.5, '', transform=ax.transAxes, ha='center')

    # Set up the plot limits and labels
    ax.set_xlim(0, 6) #SET THE LIMITS FOR THE X AXIS
    ax.set_ylim(min(y), max(y)) #SET THE LIMITS FOR THE Y AXIS
    ax.set_xlabel('x') #SET LABEL FOR X AXIS
    ax.set_ylabel('f(x)') #SET LABEL FOR Y AIXS
    ax.legend()

    # Animation update function
    def update(i):
        a, b, c = iterationArr[i]
        line.set_data([a, b], [f(a), f(b)])
        text.set_text(f'Iteration {i+1}: c = {c:.5f}')
        return line, text
    
    ani = FuncAnimation(fig, update, frames=len(iterationArr), interval=2000, repeat=False)

    plt.show()
