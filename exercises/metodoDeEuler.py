"""
2y - x = x*y'

"""

# Yn+1 = Yn + h * f(Xn, Yn)
from decimal import Decimal

def derivadaY(Yn, Xn): 
    return (2*Yn-Xn)/Xn

def eulerMethod(x_0:Decimal, y_0:Decimal, x_n:Decimal, steps: Decimal):
    values = [{"x": x_0, "y": y_0}]
    while x_0 < x_n:
        y_1 = y_0 + steps * (derivadaY(y_0, x_0))
        x_1 = x_0 + steps
        values.append({"x": x_1, "y": y_1})
        
        x_0 = x_1
        y_0 = y_1
    
    return values
    

if __name__ == "__main__":
    results = eulerMethod(Decimal("1"),Decimal("3"), Decimal("2"), Decimal("0.5"))
    for result in results:
        print(f"x: {result["x"]:.5f}",end=", ")
        print(f"y: {result["y"]:.5f}")