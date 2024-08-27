import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class utils:
    def clearTerminal():
        if os.name.upper() == "NT":
            os.system("cls")

    def printArr(arr):
        try:
            print("Iterations: ")
            for i in range(len(arr)):
                print(f"A: {arr[i][0]:.3f}, B: {arr[i][1]:.3f}, C: {arr[i][2]:.3f}")
            print("\n")
        except Exception as err:
            print(err)

class problem:

    def __init__(self, intervalStart: float, intervalEnd: float, tolerance: float) -> None:
        try:
            if(type(intervalStart) != float and type(intervalStart) != int):
                raise TypeError("Interval Start value must be Int or Float")
            if(type(intervalEnd) != float and type(intervalEnd) != int):
                raise TypeError("Interval End value must be Int or Float")
            if(type(tolerance) != float and type(tolerance) != int):
                raise TypeError("Tolerance value must be Int or Float")
            
            self.a = intervalStart
            self.b = intervalEnd
            self.tolerance = tolerance
        
        except Exception as err:
            print(err)

    def f(self, x):
        try:
            return (pow(x,2) + (1/x) - 5)
        
        except Exception as err:
            print(err)
            return None

    def bisection(self):
        try:
            a, b, = self.a, self.b
            if (self.f(a) * self.f(b) == 0):
                raise Exception("Fail")
            
            iterrationArr = []
            

            c = (a + b) / 2.0
            while(b - a) / 2.0 > self.tolerance:
                iterrationArr.append((a, b, c))
                if(self.f(c) == 0):
                    return c
                elif(self.f(a) * self.f(c) < 0):
                    b = c
                else:
                    a = c

                c = (a + b) / 2.0

            return iterrationArr
        
        except Exception as err:
            print(err)
            return None

def drawGraph(problemObj:object, data: list, yLimit:int = None, animationTimer:int = 2000):
    try:
        # Prepare the plot
        figure, ax = plt.subplots()
        x = np.linspace(1e-3, 6, 200)

        y = problemObj.f(x)
        ax.plot(x, y, 'b-', label='f(x)')
        ax.axhline(0, color='black', lw=0.5)
        line, = ax.plot([], [], 'ro-', lw=2)
        text = ax.text(0.5, 0.5, '', transform=ax.transAxes, ha='center')

        # Set up the plot limits and labels
        ax.set_xlim(0, 6) #Set limits for the X axis

        #Set limits for the Y axis
        if(yLimit == None):
            ax.set_ylim(min(y), 30) 
        else:
            ax.set_ylim(min(y), max(y))

        ax.set_xlabel('x') #Set label For X axis
        ax.set_ylabel('f(x)') #Set label for Y axis
        ax.legend()

        # Animation update
        def update(i):
            a, b, c = data[i]
            line.set_data([a, b], [problemObj.f(a), problemObj.f(b)])
            text.set_text(f'Iteration {i+1}: c = {c:.3f}')
            return line, text
        
        ani = FuncAnimation(figure, update, frames=len(data), interval=animationTimer, repeat=False)

        plt.show()
    
    except Exception as err:
        print(err)

if __name__ == "__main__":
    utils.clearTerminal()
    problemObj = problem(intervalStart=1e-3, intervalEnd=5, tolerance=1e-3)

    #Create an array that contains the values for each iteration
    iterationArr = problemObj.bisection()
    utils.printArr(iterationArr)

    drawGraph(problemObj=problemObj, data=iterationArr)