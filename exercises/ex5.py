#Uma boia esferica de volume de 10l e massa 2kg flutua em um corpo de agua
#qual a altura da parte molhada da boia

import math
import numpy as np
import matplotlib.pyplot as plt

V = 1e-2 #L
M = 2 #KG
WATER_DENSITY = 1000

def getRadius():
    try:
        radius = ((V*3)/(4*math.pi))**(1/3)
        return radius
    except Exception as err:
        print(err)
        return None
    #V = 4 * math.pi * (pow(r,3)/3)
    #V/4 = math.pi * (pow(r,3)/3)
    #pow(r,3) = V/4/math.pi*3
    #radius = pow((V/4/math.pi/3),2)
    
def getVolumeDeslocado():
    return M/WATER_DENSITY

def f(h):
    vD = getVolumeDeslocado()
    radius = getRadius()
    return ((math.pi*(h**2))/3)*(3*radius-h)-vD
    

def secantMethod(f, x0, x1, tol: float=1e-5, maxIter:int =500):
    iter = 0
    while iter < maxIter:
        # Calcula o próximo valor
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        # Checa se os valores estão dentro da tolerância desejada
        if abs(x2 - x1) < tol:
            return x2, iter + 1

        # Atualizamos os valores para a próxima iteração
        x0, x1 = x1, x2
        iter += 1
    return [x1, maxIter]  # Retorna se não houve convergência


def generateErrorNonConverge():
    res = secantMethod(f, 0.05, 100.0)
    print(f"Height: {res[0]: .9f}\nIter:{res[1]}")

def drawGraph(f, x0, x1):
    try:
        # Prepare the plot
        
        x = np.linspace(x0, x1, 200)

        y = f(x)
        plt.plot(x, y)
        plt.show()
    
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:        
        res = secantMethod(f, 0.05, 0.1)
        print(f"Height: {res[0]: .9f} meters\nIterations:{res[1]}")
        #generateErrorNonConverge()

        drawGraph(f, 0.001, 0.1)
        

    except Exception as err:
        print(err)
    
    
    