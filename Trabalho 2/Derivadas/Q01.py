import random
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

    # exato = 4 + math.log(16) # primeira derivada #esse é o valor que estamos tentando encontrar(para vies de comparacao)



    x0 = 7.1258
    x = [6.9989, 7.1355, 7.2961]
    
    
    def f(x):
        func = math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)
        return func

    n = len(x)
    k = 1 #ordem da derivada

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))
    #print(exato)

    
    