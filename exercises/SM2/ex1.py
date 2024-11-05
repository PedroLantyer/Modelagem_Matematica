def newton_raphson(f, df, x0: float, tolerance:float = 1e-1, max_iter:int = 100):
    iterations = 0

    while(iterations < max_iter):
        x1 = x0 - f(x0) / df(x0)    
        if abs(f(x1)) < tolerance:
            return [x1, (iterations+1)]
        x0 = x1
        iterations += 1
    return [x0, iterations]

def f(x):
    return (3 * pow(x,3)) + (2 * x) - 4

def df(x):
    return (9 * pow(x,2)) + 2

if __name__ == "__main__":
    [x0,iter] = newton_raphson(f=f, df=df, x0=1e-4, max_iter=4)
    print(f"x = {x0:.4f}")