def secantMethod(f, x0, x1, tol: float=1e-5, maxIter:int =100):
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

def f(x):
    return pow(x,3) - 2*pow(x,2) + 2*x - 5

if __name__ == "__main__":
    x0, x1 = 2, 1
    res = secantMethod(f, x0, x1)
    print(f"Root:{res[0]:.7f}\nIter: {res[1]}")