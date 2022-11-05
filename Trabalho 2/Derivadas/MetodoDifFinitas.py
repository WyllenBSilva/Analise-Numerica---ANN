import random
from re import X
import numpy as np
import math


# k -> ordem
def dif_fin(x, x0, k):
    n = len(x)
    A = [[1]*n]
    B = [0]
    for i in range(1,n):
        row = [xi**i for xi in x]
        A.append(row)
        if i < k:
            B.append(0)
        else:
            bi = math.factorial(i) / math.factorial(i-k) * x0**(i-k)
            B.append(bi)
    return np.linalg.solve(A, B)

def aprox(coeffs,f,x):
    return sum(ci*f(xi) for ci, xi in zip(coeffs,x))


if __name__ == '__main__':

    exato = 4 + math.log(16) # primeira derivada #esse é o valor que estamos tentando encontrar(para vies de comparacao)

    def f(x):
        return x**x 
    tol = 0.1
    a = 2 - tol
    b = 2 + tol
    n = 20 # numero de pontos
    x = [ a+(b-a)*random.random() for _ in range(n)]
    x0 = 2 #ponto onde estamos calculando a derivada
    k = 5 #ordem da derivada

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))
    print(exato)

    
    